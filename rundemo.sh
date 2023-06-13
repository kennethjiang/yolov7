#!/bin/bash

python3 detect.py --nosave --weights runs/train/yolov7-fold-3-500/weights/best.pt --conf 0.25 --img-size 800 --source $1 --device mps --view-img --exist-ok --name exp
