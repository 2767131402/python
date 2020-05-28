from concurrent.futures import ThreadPoolExecutor
from time import sleep
from random import randint


def a(n):
    print(n, 'start')
    s = randint(1, 10)  # 随机休眠s秒，模拟IO延迟
    sleep(s)
    print(n, s, 'finish')


print('test start')
with ThreadPoolExecutor(max_workers=100) as workers:  # 开100线程
    workers.map(a, range(20))
print('end')