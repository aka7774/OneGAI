#!/usr/bin/bash

git clone https://github.com/ZFTurbo/MVSEP-MDX23-music-separation-model mdx23
cd mdx23

python3 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

venv/bin/python -m pip install -r requirements.txt
