# https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform/index.html#overview
sudo apt update && sudo apt install -y autoconf bc build-essential g++-8 gcc-8 clang-8 lld-8 gettext-base gfortran-8 iputils-ping libbz2-dev libc++-dev libcgal-dev libffi-dev libfreetype6-dev libhdf5-dev libjpeg-dev liblzma-dev libncurses5-dev libncursesw5-dev libpng-dev libreadline-dev libssl-dev libsqlite3-dev libxml2-dev libxslt-dev locales moreutils openssl python-openssl rsync scons python3-pip libopenblas-dev
sudo apt-get install libopenblas-base libopenmpi-dev
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install aiohttp numpy=='1.19.4' scipy=='1.5.3'
export LD_LIBRARY_PATH="/usr/lib/llvm-8/lib:$LD_LIBRARY_PATH"
sudo python3 -m pip install --upgrade protobuf
wget -O /tmp/torch-1.10.0-cp36-cp36m-linux_aarch64.whl 'https://nvidia.box.com/shared/static/fjtbno0vpo676a25cgvuqc1wty0fkkg6.whl'
sudo python3 -m pip install --no-cache /tmp/torch-1.10.0-cp36-cp36m-linux_aarch64.whl
