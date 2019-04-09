# -*- coding: utf-8 -*-
import os
import sys
import cv2
import time
import argparse
import shutil
from keras.models import load_model
from PIL import Image
from CNN import utils

def parse_args():
    parser = argparse.ArgumentParser(description='image classifier')
    parser.add_argument('--data', dest='data_dir', default='data')
    parser.add_argument('--list', dest='list_dir', default='list')
    parser.add_argument('--model', dest='model_name', required=True)
    args = parser.parse_args()
    return args

args = parse_args()
model = load_model(args.model_name)
classes = ['bad', 'good'] #If you wanna original label,you change this list
IMG_SIZE = 128


while True:
    # Capture target object
    t1 = time.time()
    cc = cv2.VideoCapture(0)
#   cc = cv2.VideoCapture(1) ←If camera does not work,you switch this script. And you confirm camera's number.
    rr, img = cc.read()
    cv2.imwrite('tmp.png',img)
    cc.release()
    t2 = time.time()
    elapsed_time = t2-t1
    print(f"Capture Time：{elapsed_time}")
    # Predict part
    imges = []
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img/255.0
    imges.append(img)
    x_test = np.asarray(imges)
    pred = model.predict(x_test, batch_size=32, verbose=0)
    print('predict:', classes[np.argmax(pred[0])])
    t3 = time.time()
    elapsed_time = t3-t2
    print(f"Predict Time：{elapsed_time}")
    # Image update processing for UI part
    if classes[np.argmax(pred[0])] == 'good':  #If you wanna original label,you change this script
        shutil.copyfile("./prtotypeUI/images/safe.png", "./prtotypeUI/images/judge.png")
    else:
        shutil.copyfile("./prtotypeUI/images/out.png", "./prtotypeUI/images/judge.png")
    os.rename('./prtotypeUI/images/3.png','./prtotypeUI/images/4.png')
    os.rename('./prtotypeUI/images/2.png','./prtotypeUI/images/3.png')
    os.rename('./prtotypeUI/images/1.png','./prtotypeUI/images/2.png')
    os.rename('./prtotypeUI/images/predict.png','./prtotypeUI/images/1.png')
    im = Image.open('tmp.png')
    im_resize = im.resize((int(im.width / 4), int(im.height / 4)))
    im_resize.save('./prtotypeUI/images/predict.png')
    t4 = time.time()
    elapsed_time = t4-t3
    print(f"Image update processing Time：{elapsed_time}")
    time.sleep(10) #Interval of next  object
