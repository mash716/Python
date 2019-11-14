import os
import glob
from PIL import Image

from_dir  = "C:/Users/masho/Desktop/work/python/Python/lib/movie/20191114231101207027"#編集したい動画のパス
to_dir  = "C:/Users/masho/Desktop/work/python/Python/lib/movie/aaaa/"#トリミングしたい動画のパス

 
wsize = input('Image Size: ')
if wsize=='':
  wsize=700 #デフォルトは幅700px
else:
  wsize = int(wsize)
#指定フォルダのjpegファイル一覧を取得
files = glob.glob(from_dir + '/*.png')
 
#ファイル一覧をループ
for f in files:
  img = Image.open(f)
  #指定幅以下の画像はスキップ
  if wsize >= img.width:
    continue
  #指定幅からリサイズレートを算出
  rate = wsize / img.width
  #リサイズレートから高さを算出
  hsize = int(img.height * rate)
  #リサイズ実行
  img_resize = img.resize((wsize, hsize))
  #新しいファイル名を作成
  imgdir = os.path.dirname(f)
  imgname = os.path.basename(f)
  newfname = to_dir + "out_" + imgname
  print(newfname)
  #リサイズ画像を指定ファイル名で保存
  img_resize.save(newfname)