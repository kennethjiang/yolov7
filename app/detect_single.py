import cv2
import torch
import numpy as np

from models.experimental import attempt_load
from utils.general import non_max_suppression, scale_coords
from utils.datasets import letterbox

def load_model(model_path, device):
    """
    Loads the model
    :param model_path: the path to the model
    :param device: the device to use, accept string 'cpu' or 'cuda'
    :return: the model object and the stride of the model
    """
    half = device != 'cpu'  # half precision only supported on CUDA
    model = attempt_load(model_path, map_location=device)  # load FP32 model
    stride = int(model.stride.max())  # model stride

    if half:
        model.half()  # to FP16

    return model, stride

def detect_single(model, device, stride, img0, img_size=800, conf=0.1, iou=0.65):
    """
    Detects objects in a single image
    :param model: the model to use
    :param device: the device to use, accept string 'cpu' or 'cuda'
    :param stride: the stride of the model
    :param img0: Image
    :param img_size: the size of the image
    :param conf: the confidence threshold
    :param iou: the iou threshold
    :return: the predictions before and after nms, as a list of lists
    """

    # get the whwh of the original image
    gn = torch.tensor(img0.shape)[[1, 0, 1, 0]]  # normalization gain whwh

    # on cuda, use half precision
    half = device != 'cpu'

    # Padded resize
    img = letterbox(img0, img_size, stride=stride)[0]

    img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB
    img = np.ascontiguousarray(img)

    img = torch.from_numpy(img).to(device)
    img = img.half() if half else img.float()  # uint8 to fp16/32
    img /= 255.0  # 0 - 255 to 0.0 - 1.0
    if img.ndimension() == 3:
        img = img.unsqueeze(0)

    # Inference
    with torch.no_grad():   # Calculating gradients would cause a GPU memory leak
        pred = model(img)[0]

    # Apply NMS
    pred_after = non_max_suppression(pred, conf, iou, classes=None, agnostic=False)
    for det in pred_after:
        det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img0.shape).round()

    pred_after = pred_after[0].cpu().numpy().tolist()
    pred = pred[0].cpu().numpy().tolist()

    return pred, pred_after


if __name__ == '__main__':
    import argparse
    import time
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='yolov7.pt', help='model.pt path(s)')
    parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--device', default='cuda', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
    parser.add_argument('img_path', type=str, help='image file path')
    opt = parser.parse_args()
    print(opt)
    #check_requirements(exclude=('pycocotools', 'thop'))

    print('before load_model')
    model, stride = load_model(opt.weights, opt.device)
    print('after load_model')

    if os.path.isdir(opt.img_path):
        img_files = [file for file in os.listdir(opt.img_path) if file.endswith('.jpg')]
    else:
        img_files = [opt.img_path]
    
    start_time = time.time()

    for img_path in img_files:
        # get the original image
        img0 = cv2.imread(os.path.join(opt.img_path, img_path))
        pred, pred_after = detect_single(model, opt.device, stride, img0, opt.img_size, opt.conf_thres, opt.iou_thres)
        print(img_path, ': ',  pred_after)

    print("Time taken:", time.time() - start_time, "seconds")

