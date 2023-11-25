#!/usr/bin/bash

git clone https://github.com/Anjok07/ultimatevocalremovergui uvr5
cd uvr5

python3 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

venv/bin/pip install -r requirements.txt
