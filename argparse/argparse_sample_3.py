import argparse

#パーサーを作成
parser = argparse.ArgumentParser(
    prog='argparse_sample_3',#プログラム名
    usage='Demonstaration of argparser',#プログラムの利用方法
    description='description', #引数のヘルプの前に表示
    epilog='end',#引数のヘルプの後で表示
    add_help=True,#-h/-help オプションの追加
)

#引数の追加
parser.add_argument('-v','--verbose',help='select mode')

#引数の解析
args = parser.parse_args()