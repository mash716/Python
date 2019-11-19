import glob
import os
import shutil
import numpy as np

import cv2
from PIL import Image

### 設定
#ディレクトリの設定
img_dir = 'Untitled_Folder'  
out_dir = 'output' 

# その他拡張子の指定(あった方がよい)
types = ['*.png', '*.jpg', '*.jpeg', '*.bmp']
paths = []

#フォルダー内の拡張子を繰り返す
for t in types:
#フォルダー内の拡張子を取得する
    directory = paths.extend(glob.glob(os.path.join(img_dir, t)))
#ディレクトリ作成(ない場合はtrue)　
os.makedirs(out_dir, exist_ok=True)

#画像の高さと幅
img_width = 0
img_height = 0

#画像一枚あたりのトリミング量
num = 50

#ファイル数の確認
# path = os.getcwd()  
# files = os.listdir(img_dir)  
# count = len(files)

#枚数指定する(拡大する際)
for p in paths[1:200]:

    #複数の画像ファイルを開く
    img = Image.open(p)  # 読み込む
    img_width, img_height = img.size
    
    #print(p)
    #cropにて切りとる(ここに画像の処理をすると一括にできる)
    temp = img.crop(((img_width - num) // 2,
    (img_height - num) // 2,
    (img_width + num) // 2,
    (img_height + num) // 2))
    print(img_height)
    print(img_width)
    resized = temp.resize((img_width, img_height))
    #吐き出すファイルの名前とパスの指定をする
    out_path = os.path.join(out_dir, os.path.basename(p))
    #セーブする
    size = temp.save(out_path)
    size1 = temp.size
    #print(size1)
    num += 1

####連番画像を動画にする
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
video = cv2.VideoWriter('./video.mp4', fourcc, 30.0, (400, 400))

#フレーム数の指定が可能 フレームからフレームの間動かす
for i in range(1, 200):
    img = cv2.imread(out_dir +'/frame_img_{0:04d}.png'.format(i))
    img = cv2.resize(img, (400, 400))
    video.write(img)

video.release()