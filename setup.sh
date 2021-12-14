#!/bin/bash

sudo apt update && sudo apt upgrade -y
sudo rpi-update

sudo apt install -fy git python3 python3-dev \
                     x264 build-essential ffmpeg \
                     opencv-doc python3-numpy python3-scipy \
                     python3-matplotlib python3-pandas \
                     python3-nose python3-tk python3-opencv

pip3 install argparse imutils

echo -e "\n\n\n Testing OpenCV \n\n\n"

test_cv=`cat <<EOF
import cv2
print(cv2.__version__)
EOF`
python3 -c "$test_cv"
