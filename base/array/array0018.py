# frozensetはfromzenset関数を使用して通常のsetのように作成できます。ただし次の
# ようなremoveやdiscard、さらにaddやupdateなどを行おうとするとAttributeErrorが発生します。
test_set_1 = frozenset({'python','-','izm','-','com'})

# test_set_1.remove('-')
# test_set_1.discard('.')

print(test_set_1)