def exception_test(value_1, value_2):

    print('=======計算開始=======')
    
    result = 0

    try:
        result = value_1 + value_2
    except:
        print('計算出来ませんでした！')
    finally:
        print('計算終了')
    
    return result


print(exception_test(100,200))
print(exception_test(100,'200'))