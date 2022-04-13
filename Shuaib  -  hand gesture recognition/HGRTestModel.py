import cv2 as cv
import pickle
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.python.ops.numpy_ops import np_config
np_config.enable_numpy_behavior()
import PIL
from PIL import Image
import io



# load model
from pathlib import Path
HERE = Path(__file__).parent
# with open(HERE/'pickle_model.pkl', 'rb') as f:
#     model = pickle.load(f)
# model = pickle.load(open('pickle_model.pkl', 'rb'))
model = tf.keras.models.load_model('my_model')

model.summary()
classNames = ['Palm', 'I', 'Fist','Fist_Moved','Thumb','Index','Ok','Palm_moved','C','Down']
cap = cv.VideoCapture(0)

# def change_res(width, height):
#     cap.set(3, width)
#     cap.set(4, height)
#
# change_res()

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    success, img = cap.read()

    # print(img)
    if not success:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # print(img.shape)
    cv.imshow("frame", img)
    cv.waitKey(1)

    img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img = cv.resize(img, (320, 120))
    cv.imshow("GrayScale", img)
    cv.waitKey(1)

    img = img.reshape(1,120,320,1)
    prediction = model.predict(img)
    print(prediction)
    for i in range(10):
        if prediction[0,i] == 1.0:
            print(classNames[i])