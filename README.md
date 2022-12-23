# eye_mosaic

## Demo
![eye_mosaic](https://user-images.githubusercontent.com/121159170/209026626-af6ddac4-ed43-4377-83d4-50c0a04528c0.gif)

[youtube](https://www.youtube.com/watch?v=7SpeD7yOXh8)


## table of contents
- [Operation overview](https://github.com/CosmorootMcs/eye_mosaic#%E5%8B%95%E4%BD%9C%E6%A6%82%E8%A6%81)
- [Prerequisites](https://github.com/CosmorootMcs/eye_mosaic#%E5%89%8D%E6%8F%90%E3%81%A8%E3%81%99%E3%82%8B%E7%92%B0%E5%A2%83)
- [Installation](https://github.com/CosmorootMcs/eye_mosaic#%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%96%B9%E6%B3%95)
- [Usage](https://github.com/CosmorootMcs/eye_mosaic#%E5%AE%9F%E8%A1%8C%E6%89%8B%E9%A0%86)


## Operation overview
Jetson nanoに接続した USBウェブカメラ または CSIカメラの映像から人の正面の顔を検出し、  
リアルタイムで、目元 または 顔全体にモザイク処理を行います。  
複数人の顔を同時に検出することができ、モザイクの粗さをオプションで変更することもできます。  


## Prerequisites

- NVIDIA Jetson Nano Developer Kit
- USB Web Camera or Raspberry Pi Camera V2
- NVIDIA JetPack 4.6.1 or later

## Installation
Install this application.
   ```
   $ git clone https://github.com/CosmorootMcs/eye_mosaic
   ```
Install the dependent modules.
   ```
   $ pip3 install -r requirements.txt
   ```

## Usage

Check the camera number and make a note of it.
   ```
   $ ls -la /dev/video*
   ```
Navigate to the folder where you downloaded this app installation.
   ```
   $ cd eye_mosaic
   ```
Run this application with the command below. Also, use the camera number that you wrote down.  
Press Q to quit the application.

   ```
   $ python3 eye_mosaic.py [-h] [--csi]
                           [--roughness(0,99)]
                           [--camera CAMERA_NUM] [--face]
                         
     optional arguments:
       -h, --help         show this help message and exit
       --csi              use CSI camera
       -r, --roughness    roughness of the mosaic(between 0 and 100)
       -c CAMERA_NUM, --camera CAMERA_NUM
                          camera number
       -f, --face         blur a face
   ```

When you run the application, the image of the camera is output,  
and if a face is detected, it will be mosaicked.

![動画実行サンプル](https://user-images.githubusercontent.com/121159170/208865003-4bcd88eb-7852-4078-879d-f4cd0069e608.PNG)

#### オプション
ヘルプ画面を表示する
   ```
   -h, --help
   ```

CSIカメラを使用する場合はこのオプションを追加する
   ```
   --csi
   ```

モザイクの粗さを変更する 
0～99 を設定可能で、99が最も粗くなります
   ```
   -r, --roughness 
   ```

![粗さ](https://user-images.githubusercontent.com/121159170/208866923-0a131d6d-b282-4c45-9ebe-e2769be5a6a1.PNG)

使用するカメラの番号を選択する (参照：/dev/video*)
   ```
   -c *, --camera *
   ```
顔全体にモザイクをかける
   ```
   -f, --face
   ```
![顔モザイク](https://user-images.githubusercontent.com/121159170/209027050-cc40bd85-40b9-4dca-a526-306b5240bf68.png)


#### コマンド例

USBウェブカメラ(カメラ番号0)、粗さ30
   ```
   $ python3 eye_mosaic.py --camera 0 --roughness 30
   ```
csiカメラ(カメラ番号1)、粗さ80、顔全体にモザイクをかける
   ```
   $ python3 eye_mosaic.py --csi -c 1 -r 80 -f
   ```
