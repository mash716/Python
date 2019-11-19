import cv2

#from_dir  = "C:/Users/masho/Desktop/work/python/Python/lib/movie/20191114231101207027"#編集したい動画のパス
to_dir  = "C:/Users/masho/Desktop/work/python/Python/lib/movie/aaaa/"#トリミングしたい動画のパス
moviePath = "C:/Users/masho/Desktop/work/python/Python/lib/movie/videooriginalout.mp4"

# 動画から全てのフレームを切り出して保存する
movie = cv2.VideoCapture(moviePath)
# 動画のFPS、総フレーム数、幅、高さを取得する
fps = int(movie.get(cv2.CAP_PROP_FPS))
frameCnt = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(movie.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(movie.get(cv2.CAP_PROP_FRAME_HEIGHT))

for i in range(30):
    width += 1
    print(width)

for i in range(30):
    height += 1
    print(height)
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
        cv2.imwrite("{}_{}.{}".format(to_dir + "/frame_img", str(num).zfill(digit), "png"), frame)
        num += 1
    else:
        num -= 1
        break