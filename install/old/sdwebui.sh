#!/usr/bin/bash

git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui sdwebui
cd sdwebui
python3 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python
venv/bin/python -m pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118
cd models/Stable-diffusion/
wget -c  https://huggingface.co/aka7774/fp16_safetensors/resolve/main/7th_anime_v3_A-fp16-1833-2982-0018.safetensors
cd ../../

sed -i -e 's/^#export COMMANDLINE_ARGS=""/export COMMANDLINE_ARGS="--api"/' ./webui-user.sh
