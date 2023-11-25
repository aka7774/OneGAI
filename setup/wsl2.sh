#!/usr/bin/bash

sudo apt -y update
sudo apt -y upgrade

if [ ! -f /etc/wsl.conf ]; then
  sudo sh -c 'echo "[boot]\n" > /etc/wsl.conf'
  sudo sh -c 'echo "systemd=true\n" >> /etc/wsl.conf'
fi

if grep -q ~/.bashrc <<< "LD_LIBRARY_PATH=/usr/lib/wsl/lib"; then
  sed -i '1iexport LD_LIBRARY_PATH=/usr/lib/wsl/lib:$LD_LIBRARY_PATH\n' ~/.bashrc
  source ~/.bashrc
fi

curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt install -y git-lfs
git lfs install

sudo apt install -y python3-pip
sudo apt install -y python3.10-venv

sudo apt install -y ffmpeg
sudo apt install -y cmake gcc g++
sudo apt install -y ninja-build
sudo apt install -y unzip p7zip-full
sudo apt install -y libportaudio2 libasound-dev
