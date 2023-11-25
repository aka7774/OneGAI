#!/usr/bin/bash

wget https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/RVC1006Nvidia.7z
7z x RVC1006Nvidia.7z
rm RVC1006Nvidia.7z
mv RVC1006Nvidia rvc
cd rvc
