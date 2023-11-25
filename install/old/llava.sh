#!/usr/bin/bash

git clone https://github.com/haotian-liu/LLaVA.git llava
cd llava

python3 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

venv/bin/pip install -e .
venv/bin/pip install ninja
venv/bin/pip install flash-attn --no-build-isolation
