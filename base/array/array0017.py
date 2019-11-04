#セットはディクショナリと同じように「 {} 」（中カッコ）を使用します。
test_set_1 = {'python','-','izm','.','com'}
print(test_set_1)
print('------------------------')
for i in test_set_1:
    print(i)

#要素がない空のセットを作成する時はsetを用います。
#これはディクショナリ
test_dict = {}

#これはセット
test_set = {'python'}

#空のセット「set」を使う
empty_set = set()

# 前述の通り、重複した値を持つことはできません。
# たとえば次の例では‘python’と‘izm’が重複していますが、
# そのセットの出力結果には1つだけしか存在していません。
test_set_1 = {'python','-','izm','.','com','python','izm'}
print(test_set_1)

print('-----------------------')
for i in test_set_1:
    print(i)