# #Base64でエンコードする画像のパス
# target_file=r"C:/movie/png/sample_video_img_000.png"
# #エンコードした画像の保存先パス
# encode_file=r"C:/movie/json/encode.txt"

# json モジュールのインポート
import json
# import numpy as np
import base64
# import cv2

# 画像読み込み
img_file_path = 'C:/movie/jsonpng/'
img_file_name = 'decode.png'
img = open(img_file_path+img_file_name, 'rb')
img_byte = img.read()
img_content = base64.b64encode(img_byte).decode("utf-8")

# リクエストBody作成
# リクエストBody作成
item = img_content

if item is None:
    print("not exit")
else:
    print("exit")

with open('C:/movie/json/encode0001.json', 'w') as f:
    json.dump(item, f, ensure_ascii=False, indent=4)
