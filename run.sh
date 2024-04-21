#!/usr/bin/bash

if [ ! -e venv ]; then
  bash setup/venv.sh
fi

echo `venv/bin/python get_cmd.py $1` > _.sh
bash _.sh
