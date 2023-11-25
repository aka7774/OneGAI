#!/usr/bin/bash

cd  ./apps/

if [ -f cudnn-local-repo-ubuntu2204-8.8.1.3_1.0-1_amd64.deb ]
then
    sudo dpkg -i cudnn-local-repo-ubuntu2204-8.8.1.3_1.0-1_amd64.deb
    sudo cp /var/cudnn-local-repo-*/cudnn-local-*-keyring.gpg /usr/share/keyrings/
    sudo apt-get -y update
    sudo apt-get -y install libcudnn8=8.8.1.3-1+cuda11.8
    sudo apt-get -y install libcudnn8-dev=8.8.1.3-1+cuda11.8
    sudo apt-get -y install libcudnn8-samples=8.8.1.3-1+cuda11.8
fi
