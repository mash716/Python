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
item = {
    'requests': [{
        'image': {
            'content': img_content
        },
        'features': [{
            'type': 'LABEL_DETECTION',
            'maxResults': 10,
        }]
    }]
}
# req_body = json.dumps(item)

# # Pythonオブジェクトを文字列に変換
#json_str = json.dumps(item,indent=2,ensure_ascii=False)
# with open(json_str,"wb") as f:
#     f.write("C:/movie/json/encode0001.txt")
with open('C:/movie/json/population.json', 'w') as f:
    json.dump(item, f, ensure_ascii=False, indent=4)
