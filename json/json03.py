import json
import subprocess

def jsondata():
    f = open("json01.json", 'r')

    #jsonの読み込み
    json_data = json.load(f)
    #確認
    #jsonファイルから固定値を取得
    A = json_data["yamada"]["aaa"]
    B = json_data["yamada"]["bbb"]
    C = json_data["yamada"]["ccc"]
    D = json_data["yamada"]["ddd"]

    print(A)
    print(B)
    print(C)
    print(D)

    print(A+B+C+D)

    #実行コマンドを記入
    cmd = "aaaa.py" + " -h"
    subprocess.run(cmd,shell =True)

def test():
    print("yeah")

def test1():
    print("yeah1")

def test2():
    print("yeah2")

def test3():
    print("yeah3")

def main():
    jsondata()
    test()
    test1()
    test2()
    test3()

if __name__ == "__main__":
    main()