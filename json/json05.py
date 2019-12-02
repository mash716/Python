import json
import subprocess
#global変数(固定値)
#固定のデータ格納jsonファイル
PATH = "json01.json"

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

def jsondata1():
    global PATH
    f = open(PATH, 'r')

    #jsonの読み込み
    json_data = json.load(f)
    #確認
    #jsonファイルから固定値を取得
    A = json_data["tanaka"]["aaa"]
    B = json_data["tanaka"]["bbb"]
    C = json_data["tanaka"]["ccc"]
    D = json_data["tanaka"]["ddd"]

    #実行コマンドを記入
    cmd = "aaaa.py" + " -h" + A + B + C + D
    print(cmd)
    subprocess.run(cmd,shell =True)

def jsondata2():
    global PATH
    f = open(PATH, 'r')

    #jsonの読み込み
    json_data = json.load(f)
    #確認
    #jsonファイルから固定値を取得
    A = json_data["sakana"]["aaa"]
    B = json_data["sakana"]["bbb"]
    C = json_data["sakana"]["ccc"]
    D = json_data["sakana"]["ddd"]

    #実行コマンドを記入
    cmd = "aaaa.py" + " -h" + A + B + C + D
    print(cmd)
    subprocess.run(cmd,shell =True)

def jsondata3():
    global PATH
    f = open(PATH, 'r')

    #jsonの読み込み
    json_data = json.load(f)
    #確認
    #jsonファイルから固定値を取得
    A = json_data["hirata"]["aaa"]
    B = json_data["hirata"]["bbb"]
    C = json_data["hirata"]["ccc"]
    D = json_data["hirata"]["ddd"]

    #実行コマンドを記入
    cmd = "aaaa.py" + " -h" + A + B + C + D
    print(cmd)
    subprocess.run(cmd,shell =True)

def jsondata4():
    global PATH
    f = open(PATH, 'r')

    #jsonの読み込み
    json_data = json.load(f)
    #確認
    #jsonファイルから固定値を取得
    A = json_data["ookita"]["aaa"]
    B = json_data["ookita"]["bbb"]
    C = json_data["ookita"]["ccc"]
    D = json_data["ookita"]["ddd"]

    #実行コマンドを記入
    cmd = "aaaa.py" + " -h" + A + B + C + D
    print(cmd)

    subprocess.run(cmd,shell =True)

def jsondata5():
    global PATH
    f = open(PATH, 'r')

    #jsonの読み込み
    json_data = json.load(f)
    #確認
    #jsonファイルから固定値を取得
    A = json_data["ookita"]["aaa"]
    B = json_data["ookita"]["bbb"]
    C = json_data["ookita"]["ccc"]
    D = json_data["ookita"]["ddd"]

    #実行コマンドを記入
    cmd = "aaaa.py" + " -h" + A + B + C + D
    print(cmd)
    subprocess.run(cmd,shell =True)

def jsondata6():
    global PATH
    f = open(PATH, 'r')

    #jsonの読み込み
    json_data = json.load(f)
    #確認
    #jsonファイルから固定値を取得
    A = json_data["shati"]["aaa"]
    B = json_data["shati"]["bbb"]
    C = json_data["shati"]["ccc"]
    D = json_data["shati"]["ddd"]

    #実行コマンドを記入
    cmd = "aaaa.py" + " -h" + A + B + C + D
    print(cmd)
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
    jsondata1()
    jsondata2()
    jsondata3()
    jsondata4()
    jsondata5()
    test()
    test1()
    test2()
    test3()

if __name__ == "__main__":
    main()