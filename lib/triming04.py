import os
import glob
from PIL import Image
import cv2

from_dir  = "C:/Users/masho/Desktop/work/python/Python/lib/movie/20191114231101207027"#編集したい動画のパス
to_dir  = "C:/Users/masho/Desktop/work/python/Python/lib/movie/aaaa/"#トリミングしたい動画のパス
to_dir1  = "C:/Users/masho/Desktop/work/python/Python/lib/movie/"#トリミングしたい動画のパス

 
wsize = input('Image Size: ')
if wsize=='':
    wsize=700 #デフォルトは幅700px
else:
    wsize = int(wsize)
#指定フォルダのjpegファイル一覧を取得
files = glob.glob(from_dir + '/*.png')
 
#ファイル一覧をループ
for f in files:
    img = Image.open(f)
    #指定幅以下の画像はスキップ
    if wsize >= img.width:
        continue
    #指定幅からリサイズレートを算出
    rate = wsize / img.width
    #リサイズレートから高さを算出
    hsize = int(img.height * rate)
    #リサイズ実行
    img_resize = img.resize((wsize, hsize))
    #新しいファイル名を作成
    imgdir = os.path.dirname(f)
    imgname = os.path.basename(f)
    newfname = to_dir + "out_" + imgname
    #print(newfname)
    #リサイズ画像を指定ファイル名で保存
    moviepath = img_resize.save(newfname)

# 連番画像を結合して音声なし動画を作成する
movie = cv2.VideoCapture("C:/movie01/Café_22728.mp4")

fps = int(movie.get(cv2.CAP_PROP_FPS))
frameCnt = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))
# wsize = int(movie.get(cv2.CAP_PROP_FRAME_WIDTH))
# hsize = int(movie.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("fps:" + str(fps))
print("フレーム数:" + str(frameCnt))
print("幅:" + str(wsize))
print("高さ:" + str(hsize))

digit = len(str(frameCnt))

fourcc = cv2.VideoWriter_fourcc("M","P","4","V")
video = cv2.VideoWriter(to_dir + "/tempMovie.mp4", fourcc, fps, (wsize, hsize))
for i in range(1, digit):
    img = cv2.imread((to_dir + newfname).format(i))
    img = cv2.resize(img, (wsize, hsize))
    video.write(img)

video.release()