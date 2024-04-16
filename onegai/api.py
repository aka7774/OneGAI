import os
import importlib
import json

from fastapi import Depends, Response
from pydantic import BaseModel, Field, validator

from main import app
import onegai.apibase as ab
from onegai.config import cfg
import onegai.services
from onegai.services import svc
import onegai.apps

@app.post("/api/{app}/main")
def api_main(app, args: dict) -> ab.ApiResponse:
    try:
        fn = importlib.import_module(f'func.{app}')
        (result, detail) = fn.main(args)
        return ab.res(0, result, detail)
    except Exception as e:
        return ab.res(1, str(e))

@app.post("/api/{app}/raw")
def api_raw(app, args: dict) -> ab.ApiResponse:
    try:
        fn = importlib.import_module(f'func.{app}')
        content = fn.raw(args)
        return Response(content=content, media_type="audio/wav")
    except Exception as e:
        return ab.res(1, str(e))


class AppsArgs(BaseModel):
    app: str
    
    @validator('app')
    def validate_app(cls, value):
        if not value in svc.keys():
            raise ValueError('not in service.json')
        return value

@app.post('/app/install')
def app_install(args: AppsArgs) -> ab.ApiResponse:
    if onegai.apps.install(args.app):
        return ab.res(0, 'installed')
    else:
        return ab.res(1, 'failed')

@app.post('/app/uninstall')
def app_uninstall(args: AppsArgs) -> ab.ApiResponse:
    if onegai.apps.install(args.app):
        return ab.res(0, 'uninstalled')
    else:
        return ab.res(1, 'failed')

@app.get("/config/get_json")
def config_get_json() -> Response:
    content = json.dumps(cfg)
    return Response(content=content, media_type="application/json")

@app.post("/config/set_json")
def config_set_json(args: dict) -> ab.ApiResponse:
    with open(config_json_path, 'w') as f:
        json.dump(args, f)

    return ab.res(0, 'written')


class ServiceStartStopArgs(BaseModel):
    app: str
    restart: int = 0
    
    @validator('app')
    def validate_app(cls, value):
        if not value in svc.keys():
            raise ValueError('not in service.json')
        if not os.path.exists(f'apps/{value}'):
            raise ValueError('not installed')
        if not svc[value]['active']:
            raise ValueError('not active')
        return value

@app.post('/service/start')
def service_start(args: ServiceStartStopArgs) -> ab.ApiResponse:
    result = onegai.services.start(args.app, args.restart)
    return ab.res(0, result)

@app.post("/service/stop")
def service_stop(args: ServiceStartStopArgs) -> ab.ApiResponse:
    result = onegai.services.stop(args.app)
    return ab.res(0, result)

@app.get("/service/get_json")
def service_get_json() -> Response:
    content = json.dumps(svc)
    return Response(content=content, media_type="application/json")

@app.post("/service/set_json")
def service_set_json(args: dict) -> ab.ApiResponse:
    with open(services_json_path, 'w') as f:
        json.dump(args, f)

    return ab.res(0, 'written')
