from PIL import Image
import os, glob

image_size = 50

from_dir  = "C:/Users/masho/Desktop/work/python/Python/lib/movie/20191114231101207027"#編集したい動画のパス
to_dir  = "C:/Users/masho/Desktop/work/python/Python/lib/movie/aaaa/"#トリミングしたい動画のパス

for path in glob.glob(os.path.join(from_dir, '*.png')):
    img = Image.open(path)  # 読み込み
    img = img.resize((image_size, image_size))  # リサイズ

    basename = os.path.basename(img)
    img.save(os.path.join(to_dir, basename))
