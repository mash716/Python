import argparse    # 1. argparseをインポート

parser = argparse.ArgumentParser(description='このプログラムの説明（なくてもよい）')    # 2. パーサを作る

# 3. parser.add_argumentで受け取る引数を追加していく
parser.add_argument('arg1', help='この引数の説明（なくてもよい）')    # 必須の引数を追加
parser.add_argument('arg2', help='foooo')
parser.add_argument('--arg3')    # オプション引数（指定しなくても良い引数）を追加
parser.add_argument('-a', '--arg4')   # よく使う引数なら省略形があると使う時に便利

args = parser.parse_args()    # 4. 引数を解析

print('arg1='+args.arg1)
print('arg2='+args.arg2)
print('arg3='+args.arg3)
print('arg4='+args.arg4)