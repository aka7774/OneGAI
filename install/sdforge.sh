#!/usr/bin/bash

git clone https://github.com/lllyasviel/stable-diffusion-webui-forge sdforge
cd sdforge
python3 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

cd models/Stable-diffusion/
wget -c  https://huggingface.co/cagliostrolab/animagine-xl-3.0/resolve/main/animagine-xl-3.0.safetensors
cd ../../

sed -i -e 's/^#export COMMANDLINE_ARGS=""/export COMMANDLINE_ARGS="--api"/' ./webui-user.sh
