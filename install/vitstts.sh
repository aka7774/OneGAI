#!/usr/bin/bash

git clone https://github.com/Artrajz/vits-simple-api vitstts
cd vitstts

python3 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

venv/bin/python -m pip install -r requirements.txt
