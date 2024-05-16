from multiprocessing import Process
import os
import time


# 函数方式创建子进程
def sub_process(name):
    print(f'子进程PID:{os.getpid()},父进程的PID:{os.getppid()},-----{name}')
    time.sleep(1)


def sub_process2(name):
    print(f'子进程PID:{os.getpid()},父进程的PID:{os.getppid()},-----{name}')
    time.sleep(1)


if __name__ == '__main__':
    # 主进程
    print('主进程开始执行')
    for i in range(5):
        # 创建第一个子进程
        p1 = Process(target=sub_process, args=('tony',))
        # 创建第二个子进程
        p2 = Process(target=sub_process2, args=(18,))

        p1.start()
        p2.start()
        # 终止进程
        p1.terminate()
        p2.terminate()
        p1.join()
        p2.join()
    print('主进程执行结束')
