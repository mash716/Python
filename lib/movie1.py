from moviepy.editor import *

file_path = "C:/Users/masho/Desktop/work/python/Python/lib/movie/Café_22728.mp4"#編集したい動画のパス

#width = 1280
#height = 720

# X_start= 200#切り出しのスタートｘ座標

# Y_start = 0#切り出しのスタートy座標

# X_length = 1700#X_startからの切り出す長さ

# Y_length = 1440#Y_startからの切り出す長さ


#####

#左右の幅
X_start1= 0#切り出しのスタートｘ座標

#上下の切り取り
Y_start1 = 100#切り出しのスタートy座標

#ズーム
X_length1 = 1000#X_startからの切り出す長さ

#上下の幅
Y_length1 = 100#Y_startからの切り出す長さ


#save_path = "C:/Users/masho/Desktop/work/python/Python/lib/movie/sample.mp4"#トリミングしたい動画のパス
save_path1 = "C:/Users/masho/Desktop/work/python/Python/lib/movie/sample4.mp4"#トリミングしたい動画のパス


#video = (VideoFileClip(file_path).crop(x1=X_start,y1=Y_start,x2=X_length,y2=Y_length))#トリミング実行
video1 = (VideoFileClip(file_path).crop(x1=X_start1,y1=Y_start1,x2=X_length1,y2=Y_length1))#トリミング実行

#video.write_videofile(save_path,fps=29) #保存
video1.write_videofile(save_path1,fps=29) #保存

# Instance of 'VideoFileClip' has no 'crop' memberpylint(no-member)