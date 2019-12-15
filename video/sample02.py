import utility

import cv2
from PIL import Image
import numpy as np
import ffmpeg

# 動画のファイルパス(JSONから取得予定)
moviePath = "C:/Users/masho/Desktop/trireal_movie_composer2/sample/0006.mp4"
# 作成した動画の出力先ディレクトリ(JSONから取得予定または固定?)
outputPath = "C:/Users/masho/Desktop/trireal_movie_composer2/work_dir/"

# 一時作業用ディレクトリを作成する
wkDirPath = utility.makeWkDir()

# 動画から全てのフレームを切り出して保存する
movie = cv2.VideoCapture(moviePath)
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
        cv2.imwrite("{}_{}.{}".format(wkDirPath + "frame_img", str(num).zfill(digit), "png"), frame)
        num += 1
    else:
        num -= 1
        break

# 字幕やデコレーションなどの処理を行う
imgPath = "frame_img_{0:0" + str(digit) + "d}.png"

# 挿入するデコレーション画像ファイルパス
overImgPath = "C:/Users/masho/Desktop/trireal_movie_composer2/sample/frame.png"

# 挿入する画像をアルファ込みで読み込み、リサイズする
# デコレーション画像の横幅縦幅
imgSize = (640, 360)
imgPosition= (0, 0)
overImg = cv2.imread(overImgPath, cv2.IMREAD_UNCHANGED)
overImg = cv2.resize(overImg, imgSize)
cv_rgb_ol_image = cv2.cvtColor(overImg, cv2.COLOR_BGRA2RGBA)
pil_rgb_ol_image = Image.fromarray(cv_rgb_ol_image)
pil_rgba_ol_image = pil_rgb_ol_image.convert("RGBA")


# 画像を挿入する範囲だけ、1枚ずつ背景画像を読み込んで画像を追加し、上書き保存する
for i in range(0, frameCnt):
    # 背景画像を読み込み、PIL形式に変換する
    bgImg = cv2.imread(wkDirPath + imgPath.format(i))
    cv_rgb_bg_image = cv2.cvtColor(bgImg, cv2.COLOR_BGR2RGB)
    pil_rgb_bg_image = Image.fromarray(cv_rgb_bg_image )
    pil_rgba_bg_image = pil_rgb_bg_image.convert("RGBA")

    pil_rgba_bg_temp = Image.new('RGBA', pil_rgba_bg_image.size, (255, 255, 255, 0))
    pil_rgba_bg_temp.paste(pil_rgba_ol_image, imgPosition, pil_rgba_ol_image)
    result_image = Image.alpha_composite(pil_rgba_bg_image, pil_rgba_bg_temp)
    cv_bgr_result_image = cv2.cvtColor(np.asarray(result_image), cv2.COLOR_RGBA2BGRA)
    cv2.imwrite(wkDirPath + imgPath.format(i), cv_bgr_result_image)

# 連番画像を結合して音声なし動画を作成する
fourcc = cv2.VideoWriter_fourcc("M","P","4","V")
video = cv2.VideoWriter(wkDirPath + "tempMovie.mp4", fourcc, fps, (width, height))


for i in range(0, num):
    img = cv2.imread((wkDirPath + imgPath).format(i))
    img = cv2.resize(img, (width, height))
    video.write(img)

video.release()

#fadeout fadein
file_path = wkDirPath + "tempMovie.mp4"#編集したい動画のパス
save_path = "C:/Users/masho/Desktop/trireal_movie_composer2/work_dir/sample01.mp4"#outmovie

#動画全体の時間を調べる
video_info = ffmpeg.probe(file_path)
duration = float(video_info['streams'][0]['duration'])

#秒数抽出
divide_sec = duration
stream = ffmpeg.input(file_path, ss=0, t=0)

#5秒間のフェード
stream = stream.filter('fade', type='in', start_time=0, duration=2)
stream = stream.filter('fade', type='out', start_time=divide_sec-2, duration=2)

stream = ffmpeg.output(stream,  save_path)

ffmpeg.run(stream)
