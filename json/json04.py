import json
import subprocess

def jsondata():
    f = open("json01.json", 'r')

    #jsonの読み込み
    json_data = json.load(f)
    #jsonファイルから固定値を取得
    A = json_data["yamada"]["aaa"]
    B = json_data["yamada"]["bbb"]
    C = json_data["yamada"]["ccc"]
    D = json_data["yamada"]["ddd"]

    A1 = json_data["tanaka"]["aaa"]
    B1 = json_data["tanaka"]["bbb"]
    C1 = json_data["tanaka"]["ccc"]
    D1 = json_data["tanaka"]["ddd"]
    
    A2 = json_data["sakana"]["aaa"]
    B2 = json_data["sakana"]["bbb"]
    C2 = json_data["sakana"]["ccc"]
    D2 = json_data["sakana"]["ddd"]

    A3 = json_data["hirata"]["aaa"]
    B3 = json_data["hirata"]["bbb"]
    C3 = json_data["hirata"]["ccc"]
    D3 = json_data["hirata"]["ddd"]

    A4 = json_data["ookita"]["aaa"]
    B4 = json_data["ookita"]["bbb"]
    C4 = json_data["ookita"]["ccc"]
    D4 = json_data["ookita"]["ddd"]

    A5 = json_data["shati"]["aaa"]
    B5 = json_data["shati"]["bbb"]
    C5 = json_data["shati"]["ccc"]
    D5 = json_data["shati"]["ddd"]

    print(A)
    print(B)
    print(C)
    print(D)
    #実行コマンドを記入
    cmd = "aaaa.py" + " -h " + A + B + C + D
    print(cmd)
    subprocess.run(cmd,shell =True)

    print(A1)
    print(B1)
    print(C1)
    print(D1)

    #実行コマンドを記入
    cmd1 = "aaaa.py" + " -h" + A1+ B1 + C1 + D1
    print(cmd1)
    subprocess.run(cmd1,shell =True)

    print(A2)
    print(B2)
    print(C2)
    print(D2)

    #実行コマンドを記入
    cmd2 = "aaaa.py" + " -h" + A2 + B2 + C2 + D2
    print(cmd2)
    subprocess.run(cmd2,shell =True)

    print(A3)
    print(B3)
    print(C3)
    print(D3)

    #実行コマンドを記入
    cmd3 = "aaaa.py" + " -h" + A3 + B3 + C3 + D3
    print(cmd3)
    subprocess.run(cmd3,shell =True)

    print(A4)
    print(B4)
    print(C4)
    print(D4)

    #実行コマンドを記入
    cmd4 = "aaaa.py" + " -h" + A4 + B4 + C4 + D4
    print(cmd4)
    subprocess.run(cmd4,shell =True)

    print(A5)
    print(B5)
    print(C5)
    print(D5)

    #実行コマンドを記入
    cmd5 = "aaaa.py" + " -h" + A5 + B5 + C5 + D5
    print(cmd5)
    subprocess.run(cmd5,shell =True)

    print(A+B+C+D)


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