import subprocess
file_path = "C:/Users/masho/Desktop/work/python/Python/lib/movie/Café_22728.mp4"#編集したい動画のパス
save_path = "C:/Users/masho/Desktop/work/python/Python/lib/movie/sample.mp4"#トリミングしたい動画のパス

cmd2 = "ffmpeg -i " + file_path + " -vf crop=50:50:50:50 -t 10 -ss 10 " + save_path

resp2 = subprocess.run(cmd2, shell=True)
