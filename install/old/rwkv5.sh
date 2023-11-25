#!/usr/bin/bash

git clone https://huggingface.co/spaces/BlinkDL/ChatRWKV-gradio rwkv5
cd rwkv5

python3 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

venv/bin/python -m pip install -r requirements.txt
