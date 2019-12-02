# モジュールのインポート
import json

#jsonファイルの読み込み
def jsonread():
    # ファイルを開く
    json_file = open('json01.json', 'r',encoding="utf-8")
    # JSONとして読み込む
    json_obj  = json.load(json_file)
    #確認
    print(json_obj)