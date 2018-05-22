import threading

local_school = threading.local()

def process_student():
    std = local_school.student
    print('我是你爹,%s 是个狗 %s'%(std,threading.current_thread().name))
def process_thread(naem):
    local_school.student = naem
    process_student()
t1 = threading.Thread(target= process_thread, args=('那胖子',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('那思源',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
