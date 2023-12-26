#!/usr/bin/bash

git clone https://github.com/fishaudio/Bert-VITS2 bertvits2
cd bertvits2

python3 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

venv/bin/python -m pip install -r requirements.txt
