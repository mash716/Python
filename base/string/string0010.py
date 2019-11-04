#文字列の検索方法は様々です。まずは文字列の先頭が任意の文字であるかを調べます。戻り値はTrueもしくはFalseです。
#※TrueやFalseは真偽値を表します。簡単にいうと〇か×かということで〇はTrue、×はFalseになります。
test_str = 'python_izm'
print(test_str.startswith('python'))
print(test_str.startswith('izm'))

print(test_str.endswith('izm'))
