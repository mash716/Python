#'ffmpeg -i C:/movie/movieresult/video01.mp4 -i C:/movie/music/Speech_Off.wav -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 C:/movie/movieresult/output.mp4'
#C:/movie/movie/cup.mp4
import subprocess

cmd = 'ffmpeg -i C:/movie/movie/cup.mp4 -i C:/movie/music/Speech_Off.wav -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 C:/movie/movieresult/output02.mp4'

returncode = subprocess.call(cmd)