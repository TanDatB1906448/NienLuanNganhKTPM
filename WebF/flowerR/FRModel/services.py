from flask import request, current_app, jsonify
from tensorflow import keras
from keras.models import load_model
import cv2
import numpy as np
import os

flowers = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
model = load_model(os.path.dirname(__file__) + r"\model.h5")


def predictAImage(imgPath):
    try:
        img = cv2.imread(imgPath, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (150, 150))
        img = np.reshape(img, [1, 150, 150, 3])

        pred = model.predict(img)
        # print({flowers[x] : pred[0][x] for x in range(len(flowers))})
        return jsonify({flowers[x] : int(pred[0][x]) for x in range(len(flowers))})
    except: return None