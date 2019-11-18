import datetime
import os
import shutil
import cv2
import numpy as np
from PIL import Image

#####画像データ#####
#元動画
originpath = "C:/Users/masho/Desktop/work/python/Python/lib/movie/videooriginal.mp4"
faramedir = "C:/Users/masho/Desktop/work/python/Python/lib/movie/"
#後動画
aftermoviedir = "C:/Users/masho/Desktop/work/python/Python/lib"
afterpath = aftermoviedir + "/videoresult.pm4"
# 一時作業用ディレクトリを作成する
now = datetime.datetime.now()
wkDirPath = faramedir + "{0:%Y%m%d%H%M%S%f}".format(now)
os.makedirs(wkDirPath, exist_ok=False)
#結果ファイルとパス
print("{0:%Y%m%d%H%M%S%f}".format(now))
print(wkDirPath)
#作成ファイル定義
mkfiles = "{0:%Y%m%d%H%M%S%f}".format(now)


######動画の全フレームレートを特定のフォルダーに保存######
# 元動画の情報を取得
movie = cv2.VideoCapture(originpath)
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
#frameCntはstrの型式にするint→strはstr(XXXX)
digit = len(str(frameCnt))
#初期値num=0
num = 0
while True:
    ret, frame = movie.read()
    if ret:
        cv2.imwrite("{}_{}.{}".format(wkDirPath + "/frame_img", str(num).zfill(digit), "png"), frame)
        num += 1
    else:
        num -= 1
        break
#numの値の確認
print(num)


######上記の画像を(1枚)取得する######
image = np.asarray(Image.open(wkDirPath + "/frame_img_235.png").convert("RGB"), dtype=np.uint8)
zoomed_image = image.repeat(2, axis=0).repeat(2, axis=1)
Image.fromarray(zoomed_image).save("C:/Users/masho/Desktop/work/python/Python/lib/frame_img_235_zoomed.png")

# directory = os.listdir(wkDirPath)
# #全10回
# listfile_Be = 20
# listfile_Af = 30
# #20～29のファイルを配列で取得
# print(directory[listfile_Be:listfile_Af])
# for item in directory:
#     print(item)
# #上記の配列の要素数を定義
# dirlist = len(directory[listfile_Be:listfile_Af])
# print(dirlist)




#作業用ディレクトリを削除する
#shutil.rmtree(wkDirPath)
