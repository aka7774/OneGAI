#!/usr/bin/bash

git clone https://huggingface.co/spaces/aka7774/whisper
cd whisper

python3 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

venv/bin/python -m pip install gradio
venv/bin/python -m pip install -r requirements.txt
