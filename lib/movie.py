import datetime
import os
import shutil
import subprocess

import cv2
import moviepy.editor as mp
from PIL import Image, ImageDraw, ImageFont
from pydub import AudioSegment

# jsonファイルを読み込んで必要な情報を取得する

# 動画のファイルパス(JSONから取得予定)
moviePath = "c:/movie01/Café_22728.mp4"
musicpath = "c:/movie01/"
# 作成した動画の出力先ディレクトリ(JSONから取得予定または固定?)
outputPath = "c:/output/"
#作成後ファイル
outputPath01 = "c:/output/newMovie.mp4"


# 一時作業用ディレクトリを作成する
now = datetime.datetime.now()
wkDirPath = outputPath + "{0:%Y%m%d%H%M%S%f}".format(now)
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
    font = ImageFont.truetype("C:/Windows/Fonts/meiryob.ttc", fontSize)
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
    + " -itsoffset 00:00:05 -vol 300 -stream_loop 4 -i " + musicpath + "/Ring06.wav" \
    + " -itsoffset 00:00:15 -vol 100 -stream_loop 1 -i " + musicpath + "/Ring09.wav" \
    + " -async 1 -filter_complex amix=inputs=2:dropout_transition=2 " + outputPath + "/newMovie.mp4"

    # + " -itsoffset 00:00:15 -i " + input_audio_file1 \
    # + " -itsoffset 00:00:05 -stream_loop 10 -i " + input_audio_file3 \
resp = subprocess.run(cmd, shell=True)

#合成動画の音楽抽出
clip_input = mp.VideoFileClip(outputPath01).subclip()
clip_input.audio.write_audiofile(wkDirPath + "/input.wav")

#作成後の動画の見どころの音をのみを取得
# mp3ファイルの読み込み
sound = AudioSegment.from_file(wkDirPath + "/input.wav", format="wav")

sound01 = 5000
sound02 = 10000
sound00 = -10000

# 5000ms～10000ms(5～10秒)を抽出
sound1 = sound[sound01:sound02]

# 最後の10000ms(10秒)を抽出
sound2 = sound[sound00:]

sound03 = sound1 + sound2
# 抽出した部分を出力
sound1.export(wkDirPath + "/output1.wav", format="wav")
sound2.export(wkDirPath + "/output2.wav", format="wav")
sound03.export(wkDirPath + "/output3.wav", format="wav")

#見どころ動画の抽出
cmd1 = "ffmpeg -i " + outputPath01 + " -ss 00:00:05.000 -t 00:00:10.000 -c copy " + outputPath + "/out0001.mp4"
resp1 = subprocess.run(cmd1, shell=True)

cmd2 = "ffmpeg -i " + outputPath01 + " -t 00:00:10.000 -c copy " + outputPath + "/out0002.mp4"
resp2 = subprocess.run(cmd2, shell=True)

#動画の連結無音
outputPath11 = outputPath + "/out0001.mp4"
outputPath12 = outputPath + "/out0002.mp4"
outputPathresult = outputPath + "/out0003.mp4"

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
movie = cv2.VideoCapture(outputPath11)    
fps    = movie.get(cv2.CAP_PROP_FPS)
height = movie.get(cv2.CAP_PROP_FRAME_HEIGHT)
width  = movie.get(cv2.CAP_PROP_FRAME_WIDTH)
print(fps, int(width), int(height))

out = cv2.VideoWriter(outputPathresult, int(fourcc), fps, (int(width), int(height)))

for i in range(1,3):
    if i==1:
        movie = cv2.VideoCapture(outputPath11)
        print(movie)
        print(i)
    elif i==2:
        movie = cv2.VideoCapture(outputPath12)
        print(movie)
        print(i)  

    # 最初の1フレームを読み込む
    print(movie.isOpened())
    if movie.isOpened() == True:
        ret,frame = movie.read()
        # フレームの読み込みに成功している間フレームを書き出し続ける
        while ret == True:
            a = cv2.putText(frame, '', (400,400), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 2)
            if a is None:
                print("not exit")
            else:
                print("exit")

            # 読み込んだフレームを書き込み
            out.write(frame)
            # 次のフレームを読み込み
            ret,frame = movie.read()
# 作業用ディレクトリを削除する
shutil.rmtree(wkDirPath)
