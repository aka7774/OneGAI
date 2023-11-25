#!/usr/bin/bash

mkdir langflow
cd langflow

python3.10 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

venv/bin/python -m pip install langflow
#venv/bin/python -m pip install langflow[local]
