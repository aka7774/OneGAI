#!/usr/bin/bash

cd  ./apps/

if [ ! -f cuda-repo-ubuntu2204-11-8-local_11.8.0-520.61.05-1_amd64.deb ]
then
    wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda-repo-ubuntu2204-11-8-local_11.8.0-520.61.05-1_amd64.deb
fi
sudo dpkg -i cuda-repo-ubuntu2204-11-8-local_11.8.0-520.61.05-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2204-11-8-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get -y update
sudo apt-get -y install cuda
