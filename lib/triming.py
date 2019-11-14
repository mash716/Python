from PIL import Image
import datetime
import os
import cv2
import glob

output = "C:/Users/masho/Desktop/work/python/Python/lib/movie/"#編集したい動画のパス
moviepath = "C:/Users/masho/Desktop/work/python/Python/lib/movie/Café_22728.mp4"
save_path = "C:/Users/masho/Desktop/work/python/Python/lib/movie/sample.mp4"#トリミングしたい動画のパス
#save_path1 =  "C:/Users/masho/Desktop/work/python/Python/lib/movie/aaaa/"
save_path1 =  "triming.py/movie/aaaa/"
# 一時作業用ディレクトリを作成する
now = datetime.datetime.now()
wkDirPath = output + "{0:%Y%m%d%H%M%S%f}".format(now)
os.makedirs(wkDirPath, exist_ok=False)

# 動画から全てのフレームを切り出す
movie = cv2.VideoCapture(moviepath)
frameCnt = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))

# フレームの桁数を取得し、画像ファイルに保存する
digit = len(str(frameCnt))
num = 0
while True:
    ret, frame = movie.read()
    if ret:
        cv2.imwrite("{}_{}.{}".format(wkDirPath + "/frame_img", str(num).zfill(digit), "png"), frame)
        num += 1
    else:
        num -= 1
        break
files = glob.glob(wkDirPath + "/*.png")
for file in files:
    im = Image.open(file)
    im = im.resize((100, 100))
    im.save(save_path1 +  '*.png')
    # im_crop = im.crop((100, 100, 100, 100))
    # im_crop.save(save_path1, quality=95)
