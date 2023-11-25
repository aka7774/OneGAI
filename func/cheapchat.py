import os
import requests
import json

from onegai.config import cfg
from onegai.services import svc

app_name = os.path.splitext(os.path.basename(__file__))[0]

def main(payload: dict):
    port = svc[app_name]['port']
    response = requests.post(url=f'http://127.0.0.1:{port}/api/chat', json=payload)
    if response.status_code == 200:
        print(response.content.decode())
    else:
        raise ValueError(f'httpd status {response.status_code}')

    return response.content.decode(), {}
