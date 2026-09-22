import os
import time
from multiprocessing import Process, Lock, RLock

def speak(lock):
    # 上锁：如果锁是空闲的，立刻上锁，继续往下执行；如果锁被别人拿着：当前进程会阻塞等待（原地等）
    for i in range(10):
        lock.acquire()
        lock.acquire() # 这里直接用Lock会卡住，锁不可重入，需要用RLock
        print('好好', end='')
        print('学习', end='')
        print('天天', end='')
        print('向上')
        lock.release()
        lock.release()
        time.sleep(1)
def study(lock):
    for i in range(15):
        # with lock: 会自动完成两件事：
        #   (1).进入前：自动执行 lock.acquire() 上锁
        #   (2).离开后：自动执行 lock.release() 释放锁
        # 好处：即便代码块里发生异常，也能保证释放锁，避免“卡死”
        # 备注：RLock 可以多次上锁
        with lock:
            print('A', end='')
            print('B', end='')
            print('C', end='')
            print('D')
        time.sleep(1)

if __name__ == '__main__':
    print('我是主进程中的【第一行】打印')
    # lock = Lock()
    lock = RLock()
    p1 = Process(target=speak, args=(lock,))
    p2 = Process(target=study, args=(lock,))
    p1.start()
    p2.start()
    print('我是主进程中的【最后一行】打印')

