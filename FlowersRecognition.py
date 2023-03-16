import os

import numpy as np
from sklearn.model_selection import train_test_split
import tqdm
import cv2
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, Dense, MaxPooling2D, Flatten, Activation
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator

import matplotlib.pyplot as plt #thu vien doc anh va ghi anh
import random as rn


dataPath = "./flowers"

daisysPath = "./flowers/daisy"
dandelionsPath = "./flowers/dandelion"
rosesPath = "./flowers/rose"
sunflowersPath = "./flowers/sunflower"
tulipsPath = "./flowers/tulip"

imgSize = 150

X = []
Y = []
lables = []

def loadData(path, flowerType):
    for img in os.listdir(path):
        imgsPath = os.path.join(path, img)
        img = cv2.imread(imgsPath, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (imgSize, imgSize))

        X.append(img)
        lables.append(str(flowerType))

def splitData(X, lables):
    X = np.array(X)
    X = X / 255
    le=LabelEncoder()
    Y=le.fit_transform(lables)
    Y=to_categorical(Y,5)

    x_train, x_test, y_train, y_test=train_test_split(X,Y,test_size=0.25, random_state = 42)
    return x_train, x_test, y_train, y_test

def buildModel(inputShape = (150, 150, 3)):
    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=(5, 5), activation="relu", input_shape=inputShape))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="Same"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding='Same'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Flatten())
    model.add(Dense(512, activation="relu"))
    model.add(Dense(128, activation="relu"))
    model.add(Dense(64, activation="relu"))
    model.add(Dense(32, activation="relu"))
    model.add(Dense(5, activation="softmax"))

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.summary()
    return model

#Ham hien thi random 12 anh
def showImageTablle():
    fig,ax=plt.subplots(3, 4, figsize = (6, 6))
    for i in range(3):
        for j in range (4):
            l=rn.randint(0,len(lables))
            ax[i,j].imshow(X[l])
            ax[i,j].set_title('hoa : '+lables[l], fontsize = 8)
            
    plt.tight_layout()
    plt.show()

def main():
    #load dữ liệu hoa vào mảng X (mảng chứa hình) và lables (mảng chứa tên hoa)
    loadData(daisysPath, "Daisy")
    loadData(dandelionsPath, "Dandelion")
    loadData(rosesPath, "Rose")
    loadData(sunflowersPath, "Sunflower")
    loadData(tulipsPath, "Tulip")
    # showImageTablle()
    #Mã hóa tên hoa vào mảng Y và chia tập dữ liệu ra thành tập train và tập test
    x_train, x_test, y_train, y_test = splitData(X, lables)
    #build model
    model = buildModel()
    batchSize = 64
    epochNum = 50

    dg = ImageDataGenerator(
        featurewise_center=False, # Dat gia tri dau vao thanh 0 tren tap du lieu
        samplewise_center=False, #  Dat gia tri trung binh cua moi mau thanh 0
        featurewise_std_normalization=False, #  Chia dau vao cho std cua tap du lieu
        samplewise_std_normalization=False,  #  Chia moi dau vao cho std cua no
        zca_whitening=False,  # apply ZCA whitening(tay trang)
        rotation_range=10,  # xoay hinh anh ngau nhien trong pham vi (do, 0 den 180) 
        zoom_range = 0.1, # Hinh anh thu phong ngau nhien
        width_shift_range=0.2,  # dich chuyen ngau nhien hinh anh theo chieu ngang (mot phan nho cua tong chieu rong)
        height_shift_range=0.2,  # dich chuyen ngau nhien hinh anh theo chieu doc (mot phan cua tong chieu cao)
        horizontal_flip=True,  # hinh anh lat ngau nhien 
        vertical_flip=False)  # hinh anh lat ngau nhien 
    dg.fit(x_train)

    # model.fit(x_train, y_train, batch_size= batchSize, epochs=epochNum, validation_data=(x_test, y_test))
    H = model.fit_generator(dg.flow(x_train, y_train, batch_size=batchSize), steps_per_epoch=len(x_train) // batchSize, epochs=epochNum, validation_data=(x_test, y_test))
    model.save("model1.h5")
    


if __name__ == "__main__":
    main()