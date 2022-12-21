
# -*- coding: utf-8 -*-

import time
import cv2


# 顔検出用のカスケード分類器
#cascade classifier for face detection
cascadeFilePath = './haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascadeFilePath)

# カメラ設定
#Setting camera parameters
cam = cv2.VideoCapture(0)
time.sleep(1)	# 起動待ち

# Video設定
#Setting video parameters
video_w = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
video_h = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
video_f = cam.get(cv2.CAP_PROP_FPS)
fmt = cv2.VideoWriter_fourcc('m','p','4','v')
writer = cv2.VideoWriter('movie.mp4',fmt,video_f,(video_w,video_h))

# mosaic設定
#Setting mosaic parameter
roughness = 64	#モザイクの粗さ(小さい値程モザイクが薄くなる) #coarseness of the mosaic

while(True):
    # qで終了
    #If the 'q' key is pressed, stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # 画像取得
    #Get image
    ret, frame = cam.read()
    # グレースケールに変換
    #Convert image to grayscale
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 顔認識
    #Recognize faces
    facerect = cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))

    # 顔が検出されたか
    # If the face can be recognized
    if len(facerect) > 0:

        # モザイク処理
        # blur the eyes
        for (x, y, width, height) in facerect:
            # モザイクの範囲
            # 検出した顔から目元の位置を決める
            #Determine eye coordinates from face coordinates
            xa = int (x + (width * 0.1))
            ya = int (y + (height * 0.3))
            xb = int (x + (width * 0.9))
            yb = int (y + (height * 0.5))
            xw = xb - xa
            yh = yb - ya
            # 縮小サイズ設定
            #Check reduced size
            if xw < roughness:
                xs = 1	# 最小
            else :
                xs = int(xw/roughness)
            if yh < roughness:
                ys = 1	# 最小
            else :
                ys = int(yh/roughness)
            # モザイク処理
            # blur the eyes
            face = frame[ya:yb, xa:xb] 		# モザイク範囲切り出し #Cut out the image of eyes from the image
            reduc = cv2.resize(face, (xs,yh))	# 縮小 #downsize the image of eyes
            mosaic = cv2.resize(reduc,(xw,yh))	# 拡大（元のサイズに戻す）#enlarge the image of eyes to original size
            frame[ya:yb, xa:xb]=mosaic		# モザイクで上書き #generate a combined image in which two images are superposed

    # 動画出力
    #output the video
    writer.write(frame)
    # ウィンドウに表示
    #display the image in a window
    cv2.imshow('frame', frame)


# 終了処理
#release the camera and video
writer.release()
cam.release()
cv2.destroyAllWindows()

