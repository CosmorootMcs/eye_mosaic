## DEMO
ここにデモ動画のリンクを貼る

https://youtu.be/uGfYNeE_dLY


[動画リンク](https://github.com/yoru73/eye_mosaic)


## 目次
- [動作概要](https://github.com/yoru73/eye_mosaic#%E5%8B%95%E4%BD%9C%E6%A6%82%E8%A6%81)
- [前提とする環境](https://github.com/yoru73/eye_mosaic#%E5%89%8D%E6%8F%90%E3%81%A8%E3%81%99%E3%82%8B%E7%92%B0%E5%A2%83)
- [インストール方法](https://github.com/yoru73/eye_mosaic#%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%96%B9%E6%B3%95)
- [実行手順](https://github.com/yoru73/eye_mosaic#%E5%AE%9F%E8%A1%8C%E6%89%8B%E9%A0%86)
- [サードパーティ・ライセンス](https://github.com/yoru73/eye_mosaic#%E5%AE%9F%E8%A1%8C%E6%89%8B%E9%A0%86)


## 動作概要
目線へのモザイク、顔全体へのモザイクを行うことができます。

複数人や、写真にも対応しており


## 前提とする環境

- NVIDIA Jetson Nano 開発者キット
- USB ウェブカメラ または Raspberry Pi カメラモジュール V2
- NVIDIA JetPack 4.6.1 以降


## インストール方法
ファイルのダウンロード

$ `git clone https://github.com/yoru73/eye_mosaic`

環境のインストール

$ `pip3 install -r requirements.txt`


## 実行手順

カメラの番号をチェックする

`ll /dev`

下記コマンドを実行する

$ `cd eye_mosaic`

$ `python3 eye_mosaic.py`

コマンドを実行すると、カメラの画面がポップアップする

カメラに顔が映ると、モザイクがかかる

キーボードのQを押すと終了

#### オプション
ヘルプ画面の詳細を記載しておく

`-h`
`--help`

ヘルプ画面の表示


`--csi`
csiカメラを使用する場合はこのオプションを追加する


`--roughness`

モザイクの粗さを変更する
0～99 を設定可能で、99が最も粗くなる
 
`-c`
`--camera`

使用するカメラの番号を選択する

`--face`

顔全体へのモザイクをかける

#### コマンド例

USBウェブカメラ(カメラ番号0)、粗さ30

`python3 eye_mosaic.py --roughness 30 -c 0`

csiカメラ(カメラ番号1)、粗さ80、顔全体にモザイク 

`python3 eye_mosaic.py --csi --roughness 80 -c 1 -f`


## サードパーティ・ライセンス

