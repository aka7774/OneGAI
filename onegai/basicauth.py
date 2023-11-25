import secrets
import os
import json

from fastapi import HTTPException, status, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from onegai.config import cfg

security = HTTPBasic()

def auth_basic(credentials: HTTPBasicCredentials):
    correct_username = secrets.compare_digest(
        credentials.username, cfg['username'])
    correct_password = secrets.compare_digest(
        credentials.password, cfg['password'])
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )


def verify_from_api(credentials: HTTPBasicCredentials = Depends(security)):
    auth_basic(credentials)


class AuthStaticFiles(StaticFiles):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def __call__(self, scope, receive, send) -> None:
        assert scope["type"] == "http"

        request = Request(scope, receive)
        credentials = await security(request)
        auth_basic(credentials)
        await super().__call__(scope, receive, send)
