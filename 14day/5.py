def w1(fn):
    def inner():
        print('验证')
        fn()
    return inner

def test():
    print('成功')


f = w1(test)
f()
