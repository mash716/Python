#文字列の先頭・末尾を削除した値を取得します。それぞれlstripは先頭（左から）、
# rstripは末尾（右から）の削除となり、引数なしでは空白を除去します。
#※末尾の空白の削除は出力結果ではわかりづらいので、スラッシュを付加しています。

#左を消す
print('--------------------------------')
test_str = '    python-izm.com'
print(test_str)

test_str = test_str.lstrip()
print(test_str)

test_str  = test_str.lstrip('python')
print(test_str)


print('--------------------------------')

#右を消す
test_str = 'python-izm.com    '
print(test_str + '/')

test_str = test_str.rstrip()
print(test_str + '/')

test_str = test_str.rstrip("com")
print(test_str)