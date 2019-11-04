# タプルはプログラミングにおける機能としては一般的ですが、
# 他の言語ではあまり聞かないネーミングです。
# 簡単に言うと、複数の要素から構成されそれを一つのモノとして扱える機能です。
# 後の項で解説するリストとの違いは、
# 作成した後に要素の追加や削除が出来るか出来ないかです。
# タプルの場合は作成した後の変更は不可、
# リストの場合は可と覚えておきましょう。

import datetime
#defは関数を定義する(関数作成)
def get_today():
    today = datetime.datetime.today()
    value = (today.year,today.month,today.day)

    return value

test_tuple = get_today()

print(test_tuple)
print(test_tuple[0])
print(test_tuple[1])
print(test_tuple[2])
