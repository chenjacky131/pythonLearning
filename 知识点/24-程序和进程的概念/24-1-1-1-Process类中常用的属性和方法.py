"""
name    当前进程实例别名，默认为Process-N
pid     当前进程对象的PID值
is_alive()  进程是否执行完，没执行完结果为True，否则为False
join(timeout)   等待结束或等待timeout秒
start()     启动进程
run()       如果没有指定target参数，则启动进程后，会调用父类中run方法
terminate() 强制终止进程
"""
from multiprocessing import Process
import os
import time
# 创建子进程


def sub_process(name):
    print(f'子进程PID：{os.getpid()}，父进程的PID：{os.getppid()}，------{name}')
    time.sleep(1)


def sub_process2(name):
    print(f'子进程PID：{os.getpid()}，父进程的PID：{os.getppid()}，------{name}')
    time.sleep(1)


if __name__ == '__main__':
    # 主进程
    for i in range(5):
        # 创建第一个子进程
        p1 = Process(target=sub_process, args=('ysj',))
        # 创建第二个子进程
        p2 = Process(target=sub_process2, args=(18,))
        # 调用start()启动子进程
        p1.start()
        p2.start()
        print(p1.name, '是否活跃：', p1.is_alive())
        print(p2.name, '是否活跃：', p2.is_alive())
        print(p1.name, 'pid是：', p1.pid)
        print(p2.name, 'pid是：', p2.pid)
        p1.join()   # 主进程要等待p1执行结束，阻塞的主进程
        p2.join()   # 主进程要等待p2执行结束
    print('父进程完毕')
