#!/usr/bin/bash

git clone https://github.com/comfyanonymous/ComfyUI comfyui
cd comfyui

python3 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

venv/bin/python -m pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu121
venv/bin/python -m pip install -r requirements.txt
