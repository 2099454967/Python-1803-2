from threading import Thread
import time
def tiao():
    while True:
        time.sleep(1)
        print('唱歌')

def dance():
    while True:
        time.sleep(1)
        print('跳舞')

wu = Thread(target = tiao)
a = Thread(target = dance)
wu.start()
a.start()

