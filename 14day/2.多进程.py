import os
import time
ret = os.fork()

if ret == 0:
    print("子进程%d,父进程%d"%(os.getpid(),os.getppid()))

