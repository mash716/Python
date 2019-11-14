import moviepy.editor as mpy
import PIL
from moviepy.video.fx.all import crop

file_path = "C:/Users/masho/Desktop/work/python/Python/lib/movie/Café_22728.mp4"#編集したい動画のパス
save_path = "C:/Users/masho/Desktop/work/python/Python/lib/movie/sample.mp4"#トリミングしたい動画のパス

clip = mpy.VideoFileClip(file_path)
(w, h) = clip.size
cropped_clip = crop(clip, width=1000, height=600, x_center=w/4, y_center=h/4)

cropped_clip.write_videofile(save_path)