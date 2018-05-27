from random import randint
n = randint(1,100)
i = 0
while True:
    num = int(input('请输入您要猜的数字1 - 100:'))
    i+=1
    if num < n:
        print('小了')
    elif num > n:
        print('大了')
    else:
        print('对了')
        break
    print('一共猜了%d次'%i)
