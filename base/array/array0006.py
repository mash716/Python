#removeは指定の引数に該当する要素を削除します。最初に見つかった要素のみ削除が行われる
#ので、指定の要素がリスト内に複数存在する場合は注意が必要です。

test_list_1 = ['1','2','3','2','1']
print(test_list_1)

print('------------------------------')

test_list_1.remove('2')

print(test_list_1)