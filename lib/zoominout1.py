import os
import glob
from PIL import Image
import cv2

to_dir  = "C:/Users/masho/Desktop/work/python/Python/lib/movie/bbbb/"#トリミングしたい動画のパス
moviePath = "C:/Users/masho/Desktop/work/python/Python/lib/movie/videooriginalout.mp4"

# 連番画像を結合して音声なし動画を作成する
movie = cv2.VideoCapture("C:/movie01/Café_22728.mp4")

fps = int(movie.get(cv2.CAP_PROP_FPS))
frameCnt = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))
wsize = int(movie.get(cv2.CAP_PROP_FRAME_WIDTH))
hsize = int(movie.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("fps:" + str(fps))
print("フレーム数:" + str(frameCnt))
print("幅:" + str(wsize))
print("高さ:" + str(hsize))

digit = len(str(frameCnt))

fourcc = cv2.VideoWriter_fourcc("M","P","4","V")
video = cv2.VideoWriter(to_dir + "/tempMovie.mp4", fourcc, fps, (500, 500))
for i in range(1, 790):
    img = cv2.imread('C:/Users/masho/Desktop/work/python/Python/lib/movie/aaaa/frame_img_{0:03d}.png'.format(i))
    img = cv2.resize(img, (500, 500))
    video.write(img)

video.release()