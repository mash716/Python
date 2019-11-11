import ffmpeg

fname = 'C:/movie/movie/cup.mp4'

#動画全体の時間を調べる
video_info = ffmpeg.probe(fname)
duration = float(video_info['streams'][0]['duration'])

#後半の半分だけ取り出し
divide_sec = duration / 2

stream = ffmpeg.input(fname, ss=divide_sec, t=divide_sec)

#音声取り出し
audio_stream = stream.audio

#開始から5秒かけてフェードイン
stream = stream.filter('fade', type='in', start_time=0, duration=5)
audio_stream = audio_stream.filter('afade', type='in', start_time=0, duration=5)

stream = ffmpeg.output(stream, audio_stream, 'C:/movie/movie/out01.mp4')

ffmpeg.run(stream)