def test_func(**kwargs):
    print(kwargs)

test_func(code = 100,name = 'python-izm')

print("========================\n")

def test_func1(code,name,kana,*args,**kwargs):
    print(code,name,kana)
    print(args)
    print(kwargs)

test_func1(100,'python-izm',u'ぱいそんいずむ',
'JP','US',email = 'xxxx',city = 'Tokyo')
