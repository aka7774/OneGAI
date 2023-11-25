import os
import subprocess
import re
import requests
import base64
import gc
import json
import soundfile
import time
import psutil

from fastapi import Depends, Response
from pydantic import BaseModel, Field
import gradio_client

from main import app
import onegai.apibase as ab
from onegai.basicauth import verify_from_api, AuthStaticFiles
from onegai.config import cfg
from onegai.services import svc

app_name = os.path.splitext(os.path.basename(__file__))[0]


def grclient(args: dict):
    args.setdefault('speed', 0)
    args.setdefault('tts_voice', 'ja-JP-NanamiNeural-Female')
    args.setdefault('f0_key_up', 0)
    args.setdefault('f0_method', 'rmvpe')
    args.setdefault('index_rate', 1)
    args.setdefault('protect0', 0.33)

    port = svc[app_name]['port']
    url = f"http://127.0.0.1:{port}/"
    grc = gradio_client.Client(url)
    res = grc.predict(
        args['model_name'],
        int(args['speed']),
        args['tts_text'],
        args['tts_voice'],
        float(args['f0_key_up']),
        args['f0_method'],
        float(args['index_rate']),
        float(args['protect0']),
        fn_index=0)
    return res

def raw(args: dict):
    [output_info, edge_voice, result] = grclient(args)
    body = None
    with open(result, 'rb') as fp:
        body = fp.read()

    return body

def b64(args: dict):
    body = raw(args)

    return base64.b64encode(body)

def main(args: dict):
    return base64.b64encode(ogg(args)), {}

def ogg(args: dict):
    [output_info, edge_voice, result] = grclient(args)
    [audio, sr] = soundfile.read(result)
    soundfile.write(file=f"{result}.ogg", data=audio, samplerate=sr)
    with open(f"{result}.ogg", 'rb') as fp:
        body = fp.read()

    return body
