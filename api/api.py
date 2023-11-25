import os
import importlib

from fastapi import Depends, Response
from pydantic import BaseModel, Field

from main import app
import onegai.apibase as ab
from onegai.basicauth import verify_from_api, AuthStaticFiles
from onegai.config import cfg
from onegai.services import svc

@app.post("/api/{app}/main")
def api_main(app, args: dict, _ = Depends(verify_from_api)) -> ab.ApiResponse:
    try:
        fn = importlib.import_module(f'func.{app}')
        (result, detail) = fn.main(args)
        return ab.res(0, result, detail)
    except Exception as e:
        return ab.res(1, str(e))

@app.post("/api/{app}/raw")
def api_raw(app, args: dict, _ = Depends(verify_from_api)) -> ab.ApiResponse:
    try:
        fn = importlib.import_module(f'func.{app}')
        content = fn.raw(args)
        return Response(content=content, media_type="audio/wav")
    except Exception as e:
        return ab.res(1, str(e))
