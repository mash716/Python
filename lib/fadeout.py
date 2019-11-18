import ffmpeg
import cv2

#fadeout fadein
file_path = "C:/test/result/out0001.mp4"#編集したい動画のパス
file_path1 = "C:/test/result/out0002.mp4"#編集したい動画のパス
save_path = "C:/test/result/sample.mp4"#トリミングしたい動画のパス
save_path1 = "C:/test/result/sample1.mp4"#トリミングしたい動画のパス

#動画全体の時間を調べる
video_info = ffmpeg.probe(file_path)
duration = float(video_info['streams'][0]['duration'])

video_info1 = ffmpeg.probe(file_path1)
duration1 = float(video_info1['streams'][0]['duration'])

#秒数抽出
divide_sec = duration
stream = ffmpeg.input(file_path, ss=0, t=0)

divide_sec1 = duration1
stream1 = ffmpeg.input(file_path1, ss=0, t=0)
#音声取り出し
#audio_stream = stream.audio

#開始から5秒かけてフェードインフェードアウト

stream = stream.filter('fade', type='in', start_time=0, duration=2)
stream = stream.filter('fade', type='out', start_time=divide_sec-2, duration=2)

stream1 = stream1.filter('fade', type='in', start_time=0, duration=2)
stream1 = stream1.filter('fade', type='out', start_time=divide_sec1-2, duration=2)
#音声があるとない場合で処理をする必要がある
#audio_stream = audio_stream.filter('afade', type='in', start_time=0, duration=2)
stream = ffmpeg.output(stream,  save_path)
stream1 = ffmpeg.output(stream1,  save_path1)

ffmpeg.run(stream)
ffmpeg.run(stream1)
