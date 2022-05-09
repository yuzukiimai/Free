# -*- coding: UTF-8 -*-
#http://qiita.com/Algebra_nobu/items/a488fdf8c41277432ff3
import cv2
import os


#顔の認識
f_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')
#目の認識
e_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')


# カメラの起動
cap = cv2.VideoCapture(0)

while(True):

    # 動画ストリームからフレームを取得
    ret, frame = cap.read()

    #物体認識（顔認識）の実行
    facerect = f_cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(10, 10))
    #物体認識（目認識）の実行
    eyerect = e_cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(10, 10))
    
    #検出した顔を囲む矩形の作成
    for rect in facerect:
        cv2.rectangle(frame, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), (255, 255, 255), thickness=2)
        
        text = 'face'
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(frame,text,(rect[0],rect[1]-10),font, 2, (255, 255, 255), 2, cv2.LINE_AA)
    
    #検出した目を囲む矩形の作成
    for rect in eyerect:
        cv2.rectangle(frame, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), (0, 255, 0), thickness=2)
        
        text = 'eye'
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(frame,text,(rect[0],rect[1]-10),font, 2, (0, 255, 0), 2, cv2.LINE_AA)
        
    # 表示
    cv2.imshow("Show FLAME Image", frame) 

    # qを押したら終了。
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
