FROM nvcr.io/nvidia/l4t-pytorch:r32.7.1-pth1.10-py3
WORKDIR /app
ADD requirements.txt ./
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 5000
