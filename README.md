# eye_mosaic

## Demo
![eye_mosaic](https://user-images.githubusercontent.com/121159170/209026626-af6ddac4-ed43-4377-83d4-50c0a04528c0.gif)

[youtube](https://www.youtube.com/watch?v=7SpeD7yOXh8)


## table of contents
- [Operation overview](https://github.com/CosmorootMcs/eye_mosaic#operation-overview)
- [Prerequisites](https://github.com/CosmorootMcs/eye_mosaic#prerequisites)
- [Installation](https://github.com/CosmorootMcs/eye_mosaic#installation)
- [Usage](https://github.com/CosmorootMcs/eye_mosaic#usage)


## Operation overview
The eye_mosaic project detects the front face of a person from the image of a USB webcam or CSI camera connected to Jetson nano,
Mosaic the eyes or the entire face in real time.
Multiple faces can be detected at the same time, and the coarseness of the mosaic can be changed as an option. 


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
   $ cd eye_mosaic
   
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

![動画実行サンプル_600p](https://user-images.githubusercontent.com/121159170/209489999-98afaef8-1519-4682-a2f0-21c0419940a4.png)

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

![モザイクの粗さ_600p](https://user-images.githubusercontent.com/121159170/209489907-a6c4203a-bf43-41a1-a28a-52a4b8d9e3c6.png)

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
