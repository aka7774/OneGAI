import os
import shutil
import importlib
import psutil

from fastapi import Depends, Response
from pydantic import BaseModel, Field, validator

from main import app
import onegai.apibase as ab
from onegai.basicauth import verify_from_api
from onegai.config import cfg
from onegai.services import svc
import onegai.apps

class AppsArgs(BaseModel):
    app: str
    
    @validator('app')
    def validate_app(cls, value):
        if not value in svc.keys():
            raise ValueError('not in service.json')
        return value

@app.post('/app/install')
def app_install(args: AppsArgs, _ = Depends(verify_from_api)) -> ab.ApiResponse:
    if onegai.apps.install(args.app):
        return ab.res(0, 'installed')
    else:
        return ab.res(1, 'failed')

@app.post('/app/uninstall')
def app_uninstall(args: AppsArgs, _ = Depends(verify_from_api)) -> ab.ApiResponse:
    if onegai.apps.install(args.app):
        return ab.res(0, 'uninstalled')
    else:
        return ab.res(1, 'failed')

@app.get("/config/get_json")
def config_get_json(_ = Depends(verify_from_api)) -> Response:
    content = json.dumps(cfg)
    return Response(content=content, media_type="application/json")

@app.post("/config/set_json")
def config_set_json(args: dict, _ = Depends(verify_from_api)) -> ab.ApiResponse:
    with open(config_json_path, 'w') as f:
        json.dump(args, f)

    return ab.res(0, 'written')
