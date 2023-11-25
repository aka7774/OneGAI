import os
import time
import subprocess
import tempfile
import base64
import gc
import requests
import json
import psutil

from onegai.services import svc

app_name = os.path.splitext(os.path.basename(__file__))[0]

def main(payload: dict):
    port = svc[app_name]['port']
    response = requests.post(url=f'http://127.0.0.1:{port}/sdapi/v1/txt2img', json=payload)
    if response.status_code == 200:
        #print(response.content)
        detail = json.loads(response.content)
    else:
        raise ValueError(f'httpd status {response.status_code}')

    return '', detail
