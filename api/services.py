import os
import json

from fastapi import Depends, Response
from pydantic import BaseModel, Field, validator

from main import app
import onegai.apibase as ab
from onegai.basicauth import verify_from_api
from onegai.config import cfg
import onegai.services
from onegai.services import svc

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
def service_start(args: ServiceStartStopArgs, _ = Depends(verify_from_api)) -> ab.ApiResponse:
    result = onegai.services.start(args.app, args.restart)
    return ab.res(0, result)

@app.post("/service/stop")
def service_stop(args: ServiceStartStopArgs, _ = Depends(verify_from_api)) -> ab.ApiResponse:
    result = onegai.services.stop(args.app)
    return ab.res(0, result)

@app.get("/service/get_json")
def service_get_json(_ = Depends(verify_from_api)) -> Response:
    content = json.dumps(svc)
    return Response(content=content, media_type="application/json")

@app.post("/service/set_json")
def service_set_json(args: dict, _ = Depends(verify_from_api)) -> ab.ApiResponse:
    with open(services_json_path, 'w') as f:
        json.dump(args, f)

    return ab.res(0, 'written')
