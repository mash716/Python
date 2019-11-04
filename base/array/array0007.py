#popは指定のインデックス値に存在する要素の削除を行い、削除された要素を戻り値として返します
#引数なしで使用すると末尾の要素が削除されます。

test_list_1 = ['1','2','3','2','1']
print(test_list_1)

print('---------------------------------')

print(test_list_1.pop(1))
print(test_list_1)

print(test_list_1.pop())
print(test_list_1)