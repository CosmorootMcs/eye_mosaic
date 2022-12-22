# eye_mosaic

## DEMO
![eye_mosaic](https://user-images.githubusercontent.com/121159170/209026626-af6ddac4-ed43-4377-83d4-50c0a04528c0.gif)

[![動画リンク](https://img.youtube.com/vi/7SpeD7yOXh8/0.jpg)](https://www.youtube.com/watch?v=7SpeD7yOXh8)


## 目次
- [動作概要](https://github.com/CosmorootMcs/eye_mosaic#%E5%8B%95%E4%BD%9C%E6%A6%82%E8%A6%81)
- [前提とする環境](https://github.com/CosmorootMcs/eye_mosaic#%E5%89%8D%E6%8F%90%E3%81%A8%E3%81%99%E3%82%8B%E7%92%B0%E5%A2%83)
- [インストール方法](https://github.com/CosmorootMcs/eye_mosaic#%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%96%B9%E6%B3%95)
- [実行手順](https://github.com/CosmorootMcs/eye_mosaic#%E5%AE%9F%E8%A1%8C%E6%89%8B%E9%A0%86)


## 動作概要
Jetson nanoに接続した USBウェブカメラ または CSIカメラの映像から人の正面の顔を検出し、  
リアルタイムで、目元 または 顔全体にモザイク処理を行います。  
複数人の顔を同時に検出することができ、モザイクの粗さをオプションで変更することもできます。  


## 前提とする環境

- NVIDIA Jetson Nano 開発者キット
- USB ウェブカメラ または Raspberry Pi カメラモジュール V2
- NVIDIA JetPack 4.6.1 以降


## インストール方法
ファイルのダウンロード
   ```
   $ git clone https://github.com/yoru73/eye_mosaic
   ```
環境のインストール
   ```
   $ pip3 install -r requirements.txt
   ```

## 実行手順

カメラの番号をチェックする
   ```
   $ ls -la /dev/video*
   ```
ダウンロードしたフォルダに移動します
   ```
   $ cd eye_mosaic
   ```
下記コマンドでプログラムを実行します  
プログラムを終了する場合はQキーを押してください

   ```
   $ python3 eye_mosaic.py [-h] [--csi]
                           [--roughness(0,99)]
                           [--camera CAMERA_NUM] [--face]
                         
     optional arguments:
       -h, --help         show this help message and exit
       --csi              Use CSI camera
       -r, --roughness    roughness of the mosaic(between 0 and 100)
       -c CAMERA_NUM, --camera CAMERA_NUM
                          Camera number
       -f, --face         blur a face
   ```

コマンドを実行すると、カメラの映像が出力され  
カメラに顔が映ると、モザイクがかかります

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
