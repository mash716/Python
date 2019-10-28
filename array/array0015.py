#itemsを使用するとkeyとvalueを同時に取得することができます。
test_dict_1 = {'YEAR':'2010','MONTH':'1','DAY':'20'}

print(test_dict_1)

print('=============================')

for key,value in test_dict_1.items():
    print(key,value)