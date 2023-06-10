from flask import Flask, jsonify, render_template
from PIL import Image
import random
import io
import base64
import os

from app.detect_single import *
from app.file_image_source import *

app = Flask(__name__)

#model_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'app', 'model.pt')
#model, stride = load_model(model_path, 'cuda')

@app.route('/get-text-and-image')
def get_text_and_image():
    img0 = get_next_img()

    #img_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'derived/neil-elegoo/bad-flow-F60-lt10-dog.gcode.1673047525/1673047710.775793.jpg')
    #pred, pred_after = detect_single(model, 'cuda', stride, img_path, 800, 0.1, .45)
    texts = ['Hello, World!', 'Flask is awesome!', 'Welcome to my web app!']
    random_text = random.choice(texts)

    # Convert the image to bytes
    _, image_bytes = cv2.imencode('.jpg', img0)
    image_data = image_bytes.tobytes()

    response = {
        'text': random_text,
        'image': 'data:image/jpeg;base64,' + base64.b64encode(image_data).decode('utf-8')
    }
    return jsonify(response)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

