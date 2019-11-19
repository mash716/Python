import glob
import os
import shutil
import datetime

import cv2
from PIL import Image
'''
１.処理前動画のフレームレートを格納するディレクトリ作成
２.処理後動画のフレームレートを格納するディレクトリ作成
３.処理前動画のフレームレートを抽出した動画を作成
４.動画ファイルのトリミングを行う
５.動画を作成する
'''
### 設定
#ディレクトリの設定
#元フレームレート画像格納
inputPath = 'C:/Users/masho/Desktop/work/python/Python/video/20191119221441889897/'
#結果フレーム
outputPath = 'C:/Users/masho/Desktop/work/python/Python/video/20191119221441889897_01/'
#結果動画
resultvideo = 'C:/Users/masho/Desktop/work/python/Python/video/result/'

# その他拡張子の指定(あった方がよい)
types = ['*.png', '*.jpg', '*.jpeg', '*.bmp']
paths = []

#フォルダー内の拡張子を繰り返す
for t in types:
#フォルダー内の拡張子を取得する
    directory = paths.extend(glob.glob(os.path.join(inputPath, t)))
#ディレクトリ作成(ない場合はtrue)　
os.makedirs(resultvideo, exist_ok=True)

#画像の高さと幅
img_width = 0
img_height = 0

#画像一枚あたりのトリミング量
num = 100

#ファイル数の確認
# path = os.getcwd()  
# files = os.listdir(img_dir)  
# count = len(files)

#枚数指定する(拡大する際)
for p in paths[0:1082]:

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
    out_path = os.path.join(outputPath, os.path.basename(p))
    #セーブする
    size = temp.save(out_path)
    size1 = temp.size
    #print(size1)
    num += 1

####連番画像を動画にする
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
video = cv2.VideoWriter(resultvideo + '/video01.mp4', fourcc, 30.0, (400, 400))

#フレーム数の指定が可能 フレームからフレームの間動かす
for i in range(0,1082):
    #print('C:/Users/masho/Desktop/work/python/Python/video/20191119221441889897_01/frame_img_{0:04d}.png'.format(i))
    img = cv2.imread(outputPath + '/frame_img_{0:04d}.png'.format(i))
    print(img)
    img = cv2.resize(img, (400, 400))
    print(img)
    video.write(img)

video.release()