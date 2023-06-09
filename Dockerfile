FROM nvcr.io/nvidia/l4t-pytorch:r32.7.1-pth1.9-py3
#ENV DEBIAN_FRONTEND=noninteractive
# https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform/index.html#overview
#RUN apt update && apt install -y autoconf bc build-essential g++-8 gcc-8 clang-8 lld-8 gettext-base gfortran-8 iputils-ping libbz2-dev libc++-dev libcgal-dev libffi-dev libfreetype6-dev libhdf5-dev libjpeg-dev liblzma-dev libncurses5-dev libncursesw5-dev libpng-dev libreadline-dev libssl-dev libsqlite3-dev libxml2-dev libxslt-dev locales moreutils openssl python-openssl rsync scons python3-pip libopenblas-dev
#RUN python3 -m pip install --upgrade pip
#RUN python3 -m pip install aiohttp numpy=='1.19.4' scipy=='1.5.3'
#RUN export LD_LIBRARY_PATH="/usr/lib/llvm-8/lib:$LD_LIBRARY_PATH"
#RUN python3 -m pip install --upgrade protobuf
#RUN python3 -m pip install --no-cache https://developer.download.nvidia.com/compute/redist/jp/v461/pytorch/torch-1.11.0a0+17540c5+nv22.01-cp36-cp36m-linux_aarch64.whl

WORKDIR /app
ADD requirements.txt ./
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 3333
