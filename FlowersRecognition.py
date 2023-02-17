import os
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
import tqdm
import cv2


dataPath = "./flowers"

daisysPath = "./flowers/daisy"
dandelionsPath = "./flowers/dandelion"
rosesPath = "./flowers/rose"
sunflowersPath = "./flowers/sunflower"
tulipsPath = "./flowers/tulip"

imgSize = 150

X = []
Y = []

def loadData(path, flowerType):
    for img in os.listdir(path):
        imgsPath = os.path.join(path, img)
        img = cv2.imread(imgsPath, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (imgSize, imgSize))

        X.append(np.array(img))
        Y.append(str(flowerType))

def main():
    loadData(daisysPath, "Daisy")
    print(X[0].shape)
    print(Y[0])

if __name__ == "__main__":
    main()