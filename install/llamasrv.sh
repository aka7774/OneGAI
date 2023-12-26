#!/usr/bin/bash

mkdir llamasrv
cd llamasrv

python3 -m venv venv
curl -kL https://bootstrap.pypa.io/get-pip.py | venv/bin/python

source venv/bin/activate
FORCE_CMAKE=1 CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir

venv/bin/python -m pip install uvicorn anyio starlette fastapi sse_starlette starlette_context
