import ffmpeg

#切り取りたい座標軸を選ぶ
upper_left_x = 200
# 切り取りたい区画のx座標（px）
upper_left_y = 400
# 切り取りたい区画のy座標（px）
width = 500
# 切り取りたい区画の幅（px）
height = 600
# 切り取りたい区画の高さ（px）

stream = ffmpeg.input('C:/Users/masho/Desktop/work/python/Python/lib/movie/videooriginal.mp4')
# sample.mp4に切り取りたい動画を入れる

stream = ffmpeg.crop(stream, upper_left_x, upper_left_y, width, height)

stream = ffmpeg.output(stream, 'C:/Users/masho/Desktop/work/python/Python/lib/movie/videooriginalout.mp4')
# cropoutput.mp4が切り取った動画で出てきます。

ffmpeg.run(stream, overwrite_output=True)
# overwrite_output=Trueとすることで同じファイル名の動画がすでにあっても上書きします。