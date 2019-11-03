import argparse
 
# パーサーを作る
parser = argparse.ArgumentParser(
            prog='argparseTest.py', # プログラム名
            usage='Demonstration of argparser', # プログラムの利用方法
            description='description', # 引数のヘルプの前に表示
            epilog='end', # 引数のヘルプの後で表示
            add_help=True, # -h/–help オプションの追加
            )
 
# 引数を解析する
args = parser.parse_args()