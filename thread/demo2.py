from multiprocessing.dummy import Pool as ThreadPool

def downVideo(i):
    print(i)

# 开8个线程池
pool = ThreadPool(8)
results = pool.map(downVideo, range(10))
pool.close()
pool.join()