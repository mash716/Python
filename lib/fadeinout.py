import ffmpeg

#fadeout fadein
file_path = "C:/Users/masho/Desktop/work/python/Python/lib/movie/Café_22728.mp4"#編集したい動画のパス
save_path = "C:/Users/masho/Desktop/work/python/Python/lib/movie/sample.mp4"#トリミングしたい動画のパス

#動画全体の時間を調べる
video_info = ffmpeg.probe(file_path)
duration = float(video_info['streams'][0]['duration'])

#秒数抽出
divide_sec = duration
stream = ffmpeg.input(file_path, ss=0, t=0)

#音声取り出し
audio_stream = stream.audio

#開始から5秒かけてフェードインフェードアウト
stream = stream.filter('fade', type='in', start_time=0, duration=2)
stream = stream.filter('fade', type='out', start_time=duration-2, duration=2)
audio_stream = audio_stream.filter('afade', type='in', start_time=0, duration=2)
stream = ffmpeg.output(stream, audio_stream, save_path)

ffmpeg.run(stream)