import glob
import os
import shutil
import datetime

import cv2
from PIL import Image
'''
１.処理前動画のフレームレートを格納するディレクトリ作成
２.処理後動画のフレームレートを格納するディレクトリ作成
３.処理前動画のフレームレートを抽出した動画を保存
４.３.の動画ファイルのトリミングを行う(増やしていく)
５.動画を作成する
'''
### 設定
#ディレクトリの設定
#元動画のディレクトリ
origi_dir = 'C:/Users/masho/Desktop/work/python/Python/video/movie/Ocean_20451.mp4'
#元フレームレート画像格納
outPath = 'C:/Users/masho/Desktop/work/python/Python/video/'
#倍率用フレームレート画像格納
outPath1 = 'C:/Users/masho/Desktop/work/python/Python/video/'
#結果動画
resultvideo = 'C:/Users/masho/Desktop/work/python/Python/result/'


# 元動画フレームレート一時作業用ディレクトリを作成する
now = datetime.datetime.now()
wkorigiDirPath = outPath + "{0:%Y%m%d%H%M%S%f}".format(now)
os.makedirs(wkorigiDirPath, exist_ok=False)
# 後動画フレームレート一時作業用ディレクトリを作成する
now = datetime.datetime.now()
wkafterDirPath1 = outPath + "{0:%Y%m%d%H%M%S%f}".format(now) + '_01'
os.makedirs(wkafterDirPath1, exist_ok=False)

# 動画から全てのフレームを切り出して保存する
movie = cv2.VideoCapture(origi_dir)
# 動画のFPS、総フレーム数、幅、高さを取得する
fps = int(movie.get(cv2.CAP_PROP_FPS))
frameCnt = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(movie.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(movie.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("fps:" + str(fps))
print("フレーム数:" + str(frameCnt))
print("幅:" + str(width))
print("高さ:" + str(height))
# フレームの桁数を取得し、画像ファイルに保存する
digit = len(str(frameCnt))
num = 0
while True:
    ret, frame = movie.read()
    if ret:
        cv2.imwrite("{}_{}.{}".format(wkorigiDirPath + "/frame_img", str(num).zfill(digit), "png"), frame)
        num += 1
    else:
        num -= 1
        break

# その他拡張子の指定(あった方がよい)
types = ['*.png', '*.jpg', '*.jpeg', '*.bmp']
paths = []

#フォルダー内の拡張子を繰り返す
for t in types:
#フォルダー内の拡張子を取得する
    directory = paths.extend(glob.glob(os.path.join(wkorigiDirPath, t)))
#ディレクトリ作成(ない場合はtrue)
os.makedirs(wkafterDirPath1, exist_ok=True)

#画像の高さと幅
img_width = 0
img_height = 0

#画像一枚あたりのトリミング量
num = 200

#枚数指定する(拡大する際)
for p in paths[1:1082]:

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
    out_path = os.path.join(wkafterDirPath1, os.path.basename(p))
    #セーブする
    size = temp.save(out_path)
    size1 = temp.size
    #print(size1)
    num += 1

####連番画像を動画にする
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
video = cv2.VideoWriter(resultvideo +'/video.mp4', fourcc, 30.0, (1920, 1080))

#フレーム数の指定が可能 フレームからフレームの間動かす
for i in range(0,1082):
    img = cv2.imread(wkafterDirPath1 +'/frame_img_{0:04d}.png'.format(i))
    img = cv2.resize(img, (1920, 1080))
    video.write(img)

video.release()

# 作業用ディレクトリを削除する
shutil.rmtree(wkorigiDirPath)
shutil.rmtree(wkafterDirPath1)