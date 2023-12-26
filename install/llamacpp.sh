#!/usr/bin/bash

git clone https://github.com/ggerganov/llama.cpp llamacpp
cd llamacpp

python3 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

venv/bin/python -m pip install -r requirements.txt

mkdir build
cd build
cmake .. -DLLAMA_CUBLAS=ON
cmake --build . --config Release
cp bin/main ../main
cd ..
