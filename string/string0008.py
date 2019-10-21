#文字列の左に値を埋める場合はrjustを使います。
#第一引数が埋めた後の桁数、第二引数が埋め込む文字列です。ゼロ以外の文字列も埋め込み可能です。
test_str = '1234'
print(test_str.rjust(8,'0'))
print(test_str.rjust(8,'!'))
