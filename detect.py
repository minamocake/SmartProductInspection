import os
import sys
import cv2
import time
import datetime
from keras.models import load_model
from PIL import Image
import argparse
from CNN import utils
import os
import numpy as np
import cv2
import shutil

def parse_args():
    parser = argparse.ArgumentParser(description='image classifier')
    parser.add_argument('--data', dest='data_dir', default='data')
    parser.add_argument('--list', dest='list_dir', default='list')
    parser.add_argument('--model', dest='model_name', required=True)
    args = parser.parse_args()
    return args

args = parse_args()
model = load_model(args.model_name)
classes = ['bad', 'good']
IMG_SIZE = 128


while True:
    t1 = time.time()
    now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    cc = cv2.VideoCapture(0)
#    cc = cv2.VideoCapture(1)
    rr, img = cc.read()
#    cv2.imwrite( now + '.jpg',img)
    cv2.imwrite('tmp.png',img)
    cc.release()

    t2 = time.time()
    elapsed_time = t2-t1
    print(f"キャプチャ時間：{elapsed_time}")
#####推論部分###########
    imges = []
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img/255.0
    imges.append(img)
    x_test = np.asarray(imges)
    pred = model.predict(x_test, batch_size=32, verbose=0)
    print('predict:', classes[np.argmax(pred[0])])
#####推論部分############
    t3 = time.time()
    elapsed_time = t3-t2
    print(f"推論時間：{elapsed_time}")

#####画像更新処理############

    if classes[np.argmax(pred[0])] == 'good':
        shutil.copyfile("./prtotypeUI/images/safe.png", "./prtotypeUI/images/judge.png")
    else:
        shutil.copyfile("./prtotypeUI/images/out.png", "./prtotypeUI/images/judge.png")

    os.rename('./prtotypeUI/images/3.png','./prtotypeUI/images/4.png')
    os.rename('./prtotypeUI/images/2.png','./prtotypeUI/images/3.png')
    os.rename('./prtotypeUI/images/1.png','./prtotypeUI/images/2.png')
    os.rename('./prtotypeUI/images/predict.png','./prtotypeUI/images/1.png')
#    cv2.imwrite('./prtotypeUI/images/predict.png',save)
    im = Image.open('tmp.png')
    im_resize = im.resize((int(im.width / 4), int(im.height / 4)))
    im_resize.save('./prtotypeUI/images/predict.png')
#    cv2.imwrite('./prtotypeUI/images/predict.png',tmp)

    t4 = time.time()
    elapsed_time = t4-t3
    print(f"画像更新処理時間：{elapsed_time}")
    time.sleep(10)
