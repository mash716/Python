import os
import glob
from PIL import Image
import cv2
import datetime
import shutil
#全体動画の抽出
#オリジナル動画のパス
from_path = 'C:/test/0004.mp4'
#処理前動画のフレーム画像の抽出フォルダー
to_dir = "C:/test/result/aaaa/"
#処理後動画のフレーム画像の抽出フォルダー
to_dir1 = "C:/test/result/bbbb/"
#結果ファイル格納場所
to_dir2 = "C:/test/"

#元動画フォルダーの作成
now = datetime.datetime.now()
wkDirPath =to_dir  + "{0:%Y%m%d%H%M%S%f}".format(now)
os.makedirs(wkDirPath, exist_ok=False)
print(wkDirPath)

# 動画から全てのフレームを切り出して保存する
# 元動画のパスを情報を取得するための定義
movie = cv2.VideoCapture(from_path)

# 上記の変数から元動画情報を細かく取得
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
        cv2.imwrite("{}_{}.{}".format(wkDirPath + "/frame_img", str(num).zfill(digit), "png"), frame)
        num += 1
    else:
        num -= 1
        break

#動画の情報をinputにてサイズを記入するからの場合はデフォルトで700になる
wsize = 500

#指定フォルダのjpegファイル一覧を取得
files = glob.glob(wkDirPath + '/*.png')

#後動画フォルダーの作成
# now = datetime.datetime.now()
# wkDirPath1 =to_dir1  + "{0:%Y%m%d%H%M%S%f}".format(now)
# os.makedirs(wkDirPath1, exist_ok=False)
# print(wkDirPath1)
 
#ファイル一覧をループ
for f in files:
  img = Image.open(f)
  #指定幅からリサイズレートを算出
  rate = wsize / img.width
  #リサイズレートから高さを算出
  hsize = int(img.height * rate)
  #リサイズ実行
  img_resize = img.resize((wsize, hsize))
  #新しいファイル名を作成
  imgdir = os.path.dirname(f)
  imgname = os.path.basename(f) 
  newfname = to_dir1 + "out_" + imgname
  #print(newfname)
  #リサイズ画像を指定ファイル名で保存
  moviepath = img_resize.save(newfname)

    #print(newfname)
    #カット後の変数を定義
    
# 連番画像を結合して音声なし動画を作成する
#動画のmp4に設定
out_dir = "C:/test/result/bbbb/"

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
#(200, 112)
video = cv2.VideoWriter(to_dir2 + '/video11.mp4', fourcc, 30.0,(640, 360))

for i in range(1, 1944):
    img = cv2.imread(out_dir +"/out_frame_img_{0:04d}.png".format(i))
    #print(img)
    img = cv2.resize(img,(640, 360))
    video.write(img)

video.release()
# 作業用ディレクトリを削除する
shutil.rmtree(wkDirPath)