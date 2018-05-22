from multiprocessing import Pool

import time
import os
def work():
    for i in range(3):
        time.sleep(1)
        print('我是你爸爸pid=%d'%os.getpid())

p = Pool(3)
for i in range(5):
    print(i)
    p.apply(work)
p.close()#关闭池子
p.join()
