import datetime
import os
import stat
import shutil
import ffmpeg
import subprocess

import cv2
from moviepy.video.io.VideoFileClip import VideoFileClip
from time import sleep
import random

def attachFade(filePath, outputPath, type, in_start, in_duration, out_start, out_duration):
    """
    動画にフェード効果を付与する

    Args:
        filePath str:フェード効果を付与する対象の動画のファイルパス(ファイル名まで指定)
        outputPath str:フェード効果付与後の動画の出力先ファイルパス(ファイル名まで指定)
        type str:付与するフェード効果の種類(0:フェードイン 1:フェードアウト 2:両方)
        in_start int:フェードイン開始秒
        in_duration int:フェードイン効果継続時間
        out_start int:フェードアウト開始秒
        out_duration int:フェードアウト効果継続時間
    Returns:
        なし
    """

    stream = ffmpeg.input(filePath)

    if(type == "0"):
        stream = stream.filter("fade", type="in", start_time=in_start, duration=in_duration)
    elif(type == "1"):
        stream = stream.filter("fade", type="out", start_time=out_start, duration=out_duration)
    elif(type == "2"):
        stream = stream.filter("fade", type="in", start_time=in_start, duration=in_duration)
        stream = stream.filter("fade", type="out", start_time=out_start, duration=out_duration)
    else:
        print("param error")

    stream = ffmpeg.output(stream,  outputPath)
    ffmpeg.run(stream)


def getRandom():
    """
    0～999999999999999までの間の数字を文字列としてランダムで取得する
    """
    return str(random.randint(0, 999999999999999))

# 動画のファイルパス(JSONから取得予定)
moviePath = "c:/movie/0007.mp4"
# 作成した動画の出力先ディレクトリ(JSONから取得予定または固定?)
outputPath = "c:/output/"

# 一時作業用ディレクトリを作成する
wkDirPath = "{0:%Y%m%d%H%M%S%f}".format(datetime.datetime.now())
os.makedirs(wkDirPath, exist_ok=False)

# JSONから見どころリストを受け取る想定(見どころリストには見どころの開始秒終了秒が記載されている想定)
# #1(00:00:05～00:00:13) #2(00:00:20～00:00:30) #3(00:00:44～00:01:01)
highlightList = [[5, 13],[20, 30],[44, 61]]
highlightNum = len(highlightList)
print(highlightList)
print("ハイライト数" + str(highlightNum))

movie = cv2.VideoCapture(moviePath)
fps = int(movie.get(cv2.CAP_PROP_FPS))
width = int(movie.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(movie.get(cv2.CAP_PROP_FRAME_HEIGHT))

inFileNameList = []
outFileNameList = []

for i in range(0, highlightNum):
    inFileName = getRandom() + ".mp4"
    outFileName = getRandom() + ".mp4"
    inFileNameList.append(inFileName)
    outFileNameList.append(outFileName)
    inPath = wkDirPath + "/" + inFileName
    outPath = wkDirPath + "/" + outFileName
    fromCut = highlightList[i][0]
    toCut = highlightList[i][1]
    video = VideoFileClip(moviePath).subclip(fromCut, toCut)
    video.write_videofile(inPath, fps=fps)
    # 先頭の見どころはフェードアウトのみ実行
    if(i == 0):
        # フェードアウト開始位置を算出
        start = int(highlightList[i][1] - highlightList[i][0] - 2)
        print("フェードアウト開始秒" + str(start))
        # フェードアウト処理実行(フェードアウト時間は2固定)
        attachFade(inPath, outPath, "1", 0, 0, start, 2)
    # 最後の見どころはフェードインのみ実行
    elif(i == highlightNum - 1):
        # フェードイン処理実行(フェードイン時間は2固定)
        attachFade(inPath, outPath, "0", 0, 2, 0, 0)
    # 先頭と最後以外の見どころはフェードインアウト両方実行
    else:
        start = int(highlightList[i][1] - highlightList[i][0] - 2)
        attachFade(inPath, outPath, "2", 0, 2, start, 2)


fourcc = cv2.VideoWriter_fourcc("M","P","4","V")
out = cv2.VideoWriter(outputPath + "/output.mp4", int(fourcc), fps, (int(width), int(height)))

for i in range(0, highlightNum):
    print(outFileNameList[i])
    movie = cv2.VideoCapture(wkDirPath + "/" + outFileNameList[i])

    # 最初の1フレームを読み込む
    if movie.isOpened() == True:
        ret,frame = movie.read()
    else:
        ret = False
        movie.close()
        # フレームの読み込みに成功している間フレームを書き出し続ける
    while ret:
        # 読み込んだフレームを書き込み
        out.write(frame)
        # 次のフレームを読み込み
        ret,frame = movie.read()


# 作業用ディレクトリを削除する
# shutil.rmtree(wkDirPath)