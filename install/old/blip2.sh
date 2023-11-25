#!/usr/bin/bash

git clone https://huggingface.co/spaces/Salesforce/BLIP2 blip2

python3 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

venv/bin/python -m pip install gradio
