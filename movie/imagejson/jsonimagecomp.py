# #Base64でエンコードする画像のパス
# target_file=r"C:/movie/png/sample_video_img_000.png"
# #エンコードした画像の保存先パス
# encode_file=r"C:/movie/json/encode.txt"

import cv2
import base64
import numpy as np
import io

#Base64でエンコードされたファイルのパス C:\Users\masho\Desktop\work\python\Python\movie\encodingjson\check\aaaa.json C:\movie\json
target_file=r"C:/movie/json/encode0001.json"
#デコードされた画像の保存先パス
image_file=r"C:/movie/jsonpng/decode.png"

with open(target_file,'rb') as f:
    img_base64 = f.read()

#バイナリデータ <- base64でエンコードされたデータ  
img_binary = base64.b64decode(img_base64)
jpg=np.frombuffer(img_binary,dtype=np.uint8)

#raw image <- jpg
img = cv2.imdecode(jpg, cv2.IMREAD_COLOR)

if img is None:
    print("not exit")
else:
    print("exit")

#画像を保存する場合
imgwr = cv2.imwrite(image_file,img)

if imgwr is None:
    print("not exit")
else:
    print("exit")


# #表示確認
# cv2.imshow('window title', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()