"""
实例方法：
　　isAlive(): 返回线程是否在运行。正在运行指启动后、终止前。
　　get/setName(name): 获取/设置线程名。

　　start():  线程准备就绪，等待CPU调度
　　is/setDaemon(bool): 获取/设置是后台线程（默认前台线程（False））。（在start之前设置）

　　　　如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，主线程和后台线程均停止
       　　如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止
　　start(): 启动线程。
　　join([timeout]): 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）
"""

# 第一种方式，实例化 Thread
import random
import time
import threading
from threading import Thread
def task(name):
    print("%s is running..." % name)
    time.sleep(random.randint(1, 3))
    print(threading.enumerate())
    print("%s is over....." % name)

t = Thread(target=task, args=('aaa',))
t.start()
# 调用join( )方法等待线程结束继续执行
# t.join()
print('main over....')

# 第二种方式，继承Thread类
class MyThread(Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()
        self.n = n

    def run(self):
        print("runnint task",self.n)


t1 = MyThread("t1")
t2 = MyThread("t2")

t1.start()  # runnint task t1
t2.start()  # runnint task t2