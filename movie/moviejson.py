#C:/movie/movie/image.mp4 C:/movie/png/sample_video_img_000.png (356, 369)
import base64

#Base64でエンコードする画像のパス
target_file=r"C:/movie/png/sample_video_img_000.png"
#エンコードした画像の保存先パス
encode_file=r"C:/movie/json/encode.txt"

with open(target_file,'rb') as f:
    data = f.read()
#Base64で画像をエンコード
encode=base64.b64encode(data)
with open(encode_file,"wb") as f:
    f.write(encode)
