import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import keras
import tensorflow_hub as hub


offset = 20
imgSize = 224
labels = ['A' , 'B' , 'C' , 'Ç' , 'D' , 'E' , 'F' , 'G' , 'Ğ' , 'H' , 'I' , 'İ' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'Ö' , 'P' , 'R' , 'S' , 'Ş' , 'T' , 'U' , 'Ü' , 'V' , 'Y' , 'Z']
oldX,oldY,oldW,oldH=0,0,0,0
k=30
n=1
m=1
word = ''
counter = 0
no_hand_time = 0
detector = HandDetector(maxHands=2)
model=keras.models.load_model('my_model.h5',
                              custom_objects={'KerasLayer':hub.KerasLayer})

cap = cv2.VideoCapture(0)

while True:

    success, img = cap.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)

    if hands:
        no_hand_time = 0
        m = 1
        if len(hands) == 1:
            hand = hands[0]
            x, y, w, h = hand['bbox']
            imgCrop = imgOutput[y - offset:y + h + offset, x - offset:x + w + offset]

        if len(hands) > 1:
            x1, y1, w1, h1 = hands[0]['bbox']
            x2, y2, w2, h2 = hands[1]['bbox']
            if x1 > x2 :
                a1 = x2
            else:
                a1 = x1
            if y1 > y2 :
                a2 = y2
            else:
                a2 = y1
            if x1 + w1 > x2 + w2 :
                b1 = x1 + w1
            else:
                b1 = x2 + w2
            if y1 + h1 > y2 + h2 :
                b2 = y1 + h1
            else:
                b2 = y2 + h2
            h = b2 - a2
            w = b1 - a1
            x = a1
            y = a2
            imgCrop = imgOutput[a2 - offset:b2 + offset, a1 - offset:b1 + offset]

        if max(abs(ele) for ele in [x-oldX,y-oldY,w-oldW,h-oldH])<k:
            counter+=1
            if counter > 10:
                if n==1:
                        n=0
                        whiteImage = np.ones((imgSize, imgSize, 3), np.uint8) * 255
                        if h > w:
                            fixed_w = math.ceil((w * imgSize) / h)
                            resized_img = cv2.resize(imgCrop, (fixed_w, imgSize))
                            w_gap = math.ceil((imgSize - fixed_w) / 2)
                            whiteImage[:, w_gap:w_gap + fixed_w] = resized_img
                            whiteImage = whiteImage/255
                            list1 = model.predict(whiteImage.reshape(1,224,224,3))
                            index = np.argmax(list1)

                        else:
                            fixed_h = math.ceil((h * imgSize) / w)
                            resized_img = cv2.resize(imgCrop, (imgSize, fixed_h))
                            h_gap = math.ceil((imgSize - fixed_h) / 2)
                            whiteImage[h_gap:h_gap + fixed_h, :] = resized_img
                            whiteImage = whiteImage / 255
                            list1 = model.predict(whiteImage.reshape(1, 224, 224, 3))
                            index = np.argmax(list1)
                        if max(list1[0]) > -2:
                            word += labels[index]
                            print(word)


                if max(list1[0]) > -2:
                    print(labels[index])
                    cv2.rectangle(imgOutput, (x - offset, y - offset - 50), (x - offset + 90, y - offset - 50 + 50),
                                  (255, 0, 255),cv2.FILLED)
                    cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)

                cv2.imshow('imgCrop', imgCrop)
                cv2.imshow('whiteImage', whiteImage)

        else:
            n=1
            counter=0


        oldX, oldY, oldW, oldH = x, y, w, h
        cv2.rectangle(imgOutput, (x - offset, y - offset), (x + w + offset, y + h + offset), (255, 0, 255), 4)

    else:
        no_hand_time +=1
        if no_hand_time > 10 :
            if m == 1:
                m=0
                word += ' '

    cv2.putText(imgOutput, word, (10, 470), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 0, 0), 2)
    cv2.imshow('image',imgOutput)
    key = cv2.waitKey(1)
    if key == ord('d'):
        word = word[:-1]
    if key == ord('s'):
        word += ' '
    if key == ord('q'):
        break
