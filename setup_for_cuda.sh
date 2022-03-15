#!/bin/bash
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m'
if (( $EUID != 0 )); then
	printf "${RED}[x] sudo privileges not detected!!!\n"
	printf "This must be run as root. Use: ${NC}'sudo bash $0'\n"
 	exit
fi

packages1=(
libmount1
libselinux1
)

packages2=(
libglib2.0-0
libglib2.0-bin
libglib2.0-dev-bin
libmount-dev
libselinux1-dev
)

packages3=(
libcairo2
libcairo-gobject2
libcairo-script-interpreter2
libglib2.0-dev
)

packages4=(
gir1.2-gtk-3.0
libatk-bridge2.0-dev
libatk1.0-dev
libcairo2-dev
)

packages5=(
build-essential
cmake
unzip
pkg-config
libjpeg-dev
libpng-dev
libtiff-dev
libavcodec-dev
libavformat-dev
libswscale-dev
libv4l-dev
libxvidcore-dev
libx264-dev
libgtk-3-dev
libatlas-base-dev
gfortran
python3-dev
python3
python3-pip
)

packages_2_install=""
for package in ${packages1[@]}; do
    packages_2_install="${packages_2_install} ${package}"
done
sudo apt install -fy $packages_2_install
packages_2_install=""
for package in ${packages2[@]}; do
    packages_2_install="${packages_2_install} ${package}"
done
sudo apt install -fy $packages_2_install
packages_2_install=""
for package in ${packages3[@]}; do
    packages_2_install="${packages_2_install} ${package}"
done
sudo apt install -fy $packages_2_install
packages_2_install=""
for package in ${packages4[@]}; do
    packages_2_install="${packages_2_install} ${package}"
done
sudo apt install -fy $packages_2_install
packages_2_install=""
for package in ${packages5[@]}; do
    packages_2_install="${packages_2_install} ${package}"
done
sudo apt install -fy $packages_2_install

links=(
"https://github.com/opencv/opencv/archive/4.2.0.zip"
"https://github.com/opencv/opencv_contrib/archive/4.2.0.zip"
)
outfiles=(
"opencv.zip"
"opencv_contrib.zip"
)
i=1
for link in ${links[@]}; do
    wget -O ${outfiles[i]} $link
    i=$(($i+1))
done
for file in ${outfiles[@]}; do
    unzip $file
done

mv opencv-4.2.0 opencv
mv opencv_contrib-4.2.0 opencv_contrib