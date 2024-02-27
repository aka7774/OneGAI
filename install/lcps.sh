#!/usr/bin/bash

mkdir lcps
cd lcps

python3 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

CMAKE_ARGS="-DLLAMA_CUBLAS=on" venv/bin/python -m pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir
venv/bin/python -m pip install 'llama-cpp-python[server]'

# wget https://huggingface.co/TheBloke/calm2-7B-chat-GGUF/resolve/main/calm2-7b-chat.Q4_K_M.gguf
# venv/bin/python -m llama_cpp.server --model calm2-7b-chat.Q4_K_M.gguf --host 0.0.0.0 --port 50000 --n_gpu_layers 81
