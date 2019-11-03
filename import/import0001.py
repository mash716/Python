#共通関数をlibの中に入れる
from lib import testmod

#インスタンス化
test_class_1 = testmod.TestClass()
test_class_1.test_method('1')

#インスタンス化
test_class_2 = testmod.TestClass()
test_class_2.test_method('2')
