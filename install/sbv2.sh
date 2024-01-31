#!/usr/bin/bash

git clone https://github.com/litagin02/Style-Bert-VITS2 sbv2
cd sbv2

python3 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

venv/bin/python -m pip install -r requirements.txt
