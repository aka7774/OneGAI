import os
import requests
import json
import base64

from onegai.config import cfg
from onegai.services import svc

app_name = os.path.splitext(os.path.basename(__file__))[0]

def main(args: dict):
    return base64.b64encode(raw(args)), {}

def raw(args: dict):
    wav = generate(args['style_id'], args['text'])
    return wav

def generate(style_id: int, text: str, **json_params):
    port = svc[app_name]['port']
    url = f"http://127.0.0.1:{port}/audio_query?style_id={style_id}&text={text}"
    r_post = requests.post(url)
    j = json.loads(r_post.content.decode('utf-8'))

    j.update(json_params)

    url = f'http://127.0.0.1:{port}/synthesis?style_id={style_id}&enable_interrogative_upspeak=true'
    r_post = requests.post(url, json=j)

    return r_post.content
