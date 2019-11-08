# json モジュールのインポート
import json
 
# JSON の書き出し用のサンプルオブジェクト
data = {
    'title': 'JSONの読み書き',
    'author': 'Crane & to. 株式会社',
    'items': [
        {
            'title': 'Hellow JSON',
            'description': 'まずJSONについてを学びましょう'
        },
        {
            'title': 'PythonでJSON',
            'description': 'PythonでJSONを読み書きする方法を学びましょう'
        }
    ]
}
 
# Pythonオブジェクトをファイル書き込み
savepath = 'sample.json'
with open(savepath, 'w') as outfile:
    json.dump(data, outfile)
 
# Pythonオブジェクトを文字列に変換
json_str = json.dumps(data,indent=2,ensure_ascii=False)
print(json_str)