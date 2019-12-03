import json
import subprocess
import glob
import os

#global変数(固定値)
#固定のデータ格納jsonファイル
PATH = "json01.json"
PATH01 = "C:\\Users\\masho\\Desktop\\work\\python\\Python\\json\\jsons\\*"
PATH02 = "C:\\Users\\masho\\Desktop\\work\\python\\Python\\json\\jsons\\"

#ファイル数のカウント
filesname_all = os.listdir(PATH02)  
filecount = len(filesname_all)
print(filecount)

#ファイル名の取得
print(filesname_all)

#特定の拡張子のみを取得する
files01 = glob.glob(PATH02 + '\\*.json')
filesname = [os.path.basename(x) for x in files01]
print(filesname)

def jsondata():
    global PATH
    f = open(PATH, 'r')

    #jsonの読み込み
    json_data = json.load(f)
    #確認
    #jsonファイルから固定値を取得
    A = json_data["yamada"]["aaa"]
    B = json_data["yamada"]["bbb"]
    C = json_data["yamada"]["ccc"]
    D = json_data["yamada"]["ddd"]

    #実行コマンドを記入
    cmd = "aaaa.py" + " -h" + A + B + C + D
    print(cmd)
    subprocess.run(cmd,shell =True)

def main():
    jsondata()

if __name__ == "__main__":
    main()