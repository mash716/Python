import pydub
from pydub import AudioSegment

base_sound = AudioSegment.from_file('C:/movie/output/audio.mp3', format="mp3")  # 音声を読み込み
length_seconds = base_sound.duration_seconds  # 長さを確認
base_sound.export("C:/movie/output/resultmp3/result.mp3", format="mp3")  # 保存する

first_five_second = base_sound[:5*1000]
last_ten_second = base_sound[10*1000:]