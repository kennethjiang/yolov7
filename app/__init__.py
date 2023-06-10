from flask import Flask, jsonify, render_template
from PIL import Image
import random
import io
import base64
import os

from app.detect_single import *
from app.file_image_source import *

app = Flask(__name__)

model_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'model.pt')
model, stride = load_model(model_path, 'cuda')

@app.route('/get-text-and-image')
def get_text_and_image():
    img0 = get_next_img()

    pred, pred_after = detect_single(model, 'cuda', stride, img0, 800, 0.1, .45)

    # Convert the image to bytes
    _, image_bytes = cv2.imencode('.jpg', img0)
    image_data = image_bytes.tobytes()

    response = {
        'pred': pred_after,
        'image': 'data:image/jpeg;base64,' + base64.b64encode(image_data).decode('utf-8')
    }
    return jsonify(response)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

