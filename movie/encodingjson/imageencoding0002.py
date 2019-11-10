import json

#jsonPathを開く
with open('C:/movie/json/original/japaneses.json') as f:
#jsonファイルを読み込む
    jsnlaod = json.load(f)
    #jsonデータ確認
    print(jsnlaod)

#jsonファイルを書き込む
savepath = 'C:/movie/json/result/sample.json'

#読み込んだJsonファイルを書き込む
with open(savepath, 'w') as outfile:
#引数で読み込むjsonファイルを渡すと書き込むjsonファイル(日本語でもOK)
    json.dump(jsnlaod, outfile,ensure_ascii=False,indent=4)

# Pythonオブジェクトを文字列に変換(出力確認)
json_str = json.dumps(jsnlaod,indent=2,ensure_ascii=False)
print(json_str)