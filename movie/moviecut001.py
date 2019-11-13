import cv2
import datetime
import os
import subprocess
import shutil
import moviepy.editor as mp
from PIL import ImageFont, ImageDraw, Image

# jsonファイルを読み込んで必要な情報を取得する

# 動画のファイルパス(JSONから取得予定)
moviePath = "c:/movie01/Café_22728.mp4"
# 作成した動画の出力先ディレクトリ(JSONから取得予定または固定?)
outputPath = "c:/output/"

# 一時作業用ディレクトリを作成する
now = datetime.datetime.now()
wkDirPath = "{0:%Y%m%d%H%M%S%f}".format(now)
os.makedirs(wkDirPath, exist_ok=False)


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
        cv2.imwrite("{}_{}.{}".format(wkDirPath + "/frame_img", str(num).zfill(digit), "png"), frame)
        num += 1
    else:
        num -= 1
        break


# 動画から音声のみを抽出して保存する
clip_input = mp.VideoFileClip(moviePath).subclip()
clip_input.audio.write_audiofile(wkDirPath + "/bgm.wav")


# 字幕やデコレーションなどの処理を行う
imgPath = "/frame_img_{0:0" + str(digit) + "d}.png"
# 字幕文字(JSONから取得予定)
inputText = "さんぷる字幕ABCDxyz①２Ⅲ"
# 字幕表示開始時間(JSONから取得予定)
start = 10
# 字幕表示終了時間(JSONから取得予定)
end = 15
# 字幕挿入座標(JSONから取得予定)
position = (30, 50)
# 字幕文字色(JSONから取得予定)
fontColor = (255, 255, 0)
# 字幕文字サイズ(JSONから取得予定)
fontSize = 20
# 動画再生時間を算出する(不要かも)
playTime = frameCnt / fps
# 字幕表示開始フレーム位置を算出する
startFrame = int(start * fps)
# 字幕表示終了フレーム位置を算出する
endFrame = int(end * fps)

# 字幕を挿入するフレーム画像の部分だけを読み込んで字幕を追加し、上書き保存する
for i in range(startFrame, endFrame):
    img = Image.open((wkDirPath + imgPath).format(i))
    font = ImageFont.truetype("C:\Windows\Fonts\meiryob.ttc", fontSize)
    draw = ImageDraw.Draw(img)
    draw.text((position), inputText, fontColor, font=font)
    img.save((wkDirPath + imgPath).format(i))

# 連番画像を結合して音声なし動画を作成する
fourcc = cv2.VideoWriter_fourcc("M","P","4","V")
video = cv2.VideoWriter(wkDirPath + "/tempMovie.mp4", fourcc, fps, (width, height))

for i in range(0, num):
    img = cv2.imread((wkDirPath + imgPath).format(i))
    img = cv2.resize(img, (width, height))
    video.write(img)

video.release()


# 作成した音声なし動画に音声や効果音を付与する
cmd = "ffmpeg -i " + wkDirPath + "/tempMovie.mp4" \
    + " -vol 300 -i " + wkDirPath + "/bgm.wav" \
    + " -async 1 -filter_complex amix=inputs=1:dropout_transition=2 " + outputPath + "/newMovie.mp4"

    # + " -itsoffset 00:00:15 -i " + input_audio_file1 \
    # + " -itsoffset 00:00:05 -stream_loop 10 -i " + input_audio_file3 \
resp = subprocess.run(cmd, shell=True)


# 作業用ディレクトリを削除する
shutil.rmtree(wkDirPath)