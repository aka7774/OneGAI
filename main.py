import sys
import time
import signal
import psutil

from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

import onegai.apiloader
from onegai.config import cfg
from onegai.services import svc

import gradio as gr
from app import demo

def cleanup():
    for app in svc.keys():
        if not 'port' in svc[app]:
            continue
        onegai.services.stop(app)

def sig_handler(signum, frame) -> None:
    sys.exit(1)


if cfg['disable_docs']:
    app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
else:
    app = FastAPI()

gr.mount_gradio_app(app, demo, path="/gradio")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(RequestValidationError)
async def handler(request:Request, exc:RequestValidationError):
    print(exc)
    return JSONResponse(content={}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

@app.exception_handler(Exception)
async def handler(request:Request, exc:RequestValidationError):
    print(exc)
    return JSONResponse(content={}, status_code=400)

signal.signal(signal.SIGTERM, sig_handler)
try:
    apis = onegai.apiloader.load_apis()
finally:
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    if cfg['stop_children']:
        cleanup()
    signal.signal(signal.SIGTERM, signal.SIG_DFL)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
