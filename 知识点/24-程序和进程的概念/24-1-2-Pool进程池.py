"""
进程池的原理是：
    创建一个进程池，并设置进程池中最大的进程数量。假设进程池
中最大的进程数为3，现在有10个任务需要执行，那么进程池一次可以
执行3个任务，4次即可完成全部任务的执行。
创建进程池的语法结构：
    进程池对象 = Pool(N)
Pool进程池
方法名                             功能描述
apply_async(func, args, kwargs) 使用非阻塞方式调用函数func
apply(func, args, kwargs)       使用阻塞方式调用函数func
close()                         关闭进程池，不再接收新任务
terminate()                     不管任务是否完成，立即终止
join()                          阻塞主进程，必须在terminate()或close()之后使用
"""
from multiprocessing import Process, Pool
import os
import time


def task(name):
    print(f'子进程的PID:{os.getpid()},执行的任务:{name}')
    time.sleep(1)


if __name__ == '__main__':
    # 主进程
    start = time.time()
    print('父进程开始执行')
    # 创建进程池
    p = Pool(3)
    # 创建任务
    for i in range(10):
        #   以非阻塞的方式
        # p.apply_async(func=task, args=(i,))
        # 以阻塞式的方式
        p.apply(func=task, args=(i,))
    p.close()  # 关闭进程池，不再接收新任务
    p.join()  # 阻塞父进程，等待所有的子进程执行完毕之后，才会执行父进程中的代码
    print('所有的子进程执行完毕，父进程执行结束')
    print(time.time() - start)
