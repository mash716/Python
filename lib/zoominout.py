import ffmpeg

file_path = "C:/Users/masho/Desktop/work/python/Python/lib/movie/Café_22728.mp4"#編集したい動画のパス
save_path = "C:/Users/masho/Desktop/work/python/Python/lib/movie/sample.mp4"#トリミングしたい動画のパス

#動画全体の時間を調べる
video_info = ffmpeg.probe(file_path)
duration = float(video_info['streams'][0]['duration'])

print("=======================")

print(duration)
#後半の半分だけ取り出し
divide_sec = duration
print("=======================")

print(divide_sec)

stream = ffmpeg.input(file_path, ss=divide_sec, t=divide_sec)

print("=======================")

print(stream)

#音声取り出し
audio_stream = stream.audio

#開始から5秒かけてフェードイン
stream = stream.filter('fade', type='in', start_time=0, duration=5)
print("=======================")

print(stream)

audio_stream = audio_stream.filter('afade', type='in', start_time=0, duration=5)
print("=======================")

print(audio_stream)

stream = ffmpeg.output(stream, audio_stream, save_path)
print("=======================")

print(stream)

print("=======================")

ffmpeg.run(stream)