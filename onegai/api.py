import os
import importlib
import json
import time

from fastapi import Depends, Response
from pydantic import BaseModel, Field, validator

from main import app
from onegai.config import cfg
import onegai.apps


class ApiResponse(BaseModel):
   status: int = Field(description="ステータス")
   servertime: float = Field(description="サーバー時刻")
   result: str = Field(description="結果")
   detail: dict = Field(description="詳細")

def res(status = 0, result = '', detail = {}):
    return {
        "status": status,
        "servertime": time.time(),
        "result": result,
        "detail": detail,
    }

@app.post('/install')
def api_install(app_name: str) -> ApiResponse:
    if onegai.apps.install(app_name):
        return res(0, 'installed')
    else:
        return res(1, 'failed')

@app.post('/uninstall')
def api_uninstall(app_name: str) -> ApiResponse:
    if onegai.apps.uninstall(app_name):
        return res(0, 'uninstalled')
    else:
        return res(1, 'failed')

@app.get("/config_get")
def api_config_get() -> Response:
    content = json.dumps(cfg)
    return Response(content=content, media_type="application/json")

@app.post("/config_set")
def api_config_set(args: dict) -> ApiResponse:
    with open(config_json_path, 'w') as f:
        json.dump(args, f)

    return res(0, 'written')

@app.post('/start')
def api_start(app_name: str, restart: bool = False) -> ApiResponse:
    result = onegai.apps.start(app_name, restart)
    return res(0, result)

@app.post("/stop")
def api_stop(app_name: str) -> ApiResponse:
    result = onegai.apps.stop(app_name)
    return res(0, result)
