print("========================\n")

def test_fun(*args):
    print(args)

test_fun(1,2,3,4,5)

print("========================\n")

def test_fun1(code,name,*args):
    print(code,name)
    print(args)

test_fun1(100,'python-izm','JP','US')

print("========================\n")

def test_fun2(code,name,*countries):
    print(code,name)
    print(countries)

test_fun2(100,'python-izm','JP','US')

print("========================\n")