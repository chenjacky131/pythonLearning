"""
生产者与消费者模式
    生产者与消费者模式是线程模型中的经典问题，与编程语言无关。当程序中出现了
明确的两类任务，一个任务负责生产数据，一个任务负责处理生产的数据时就可以使用改模式。
Python内置模块queue中的Queue类
方法                              功能描述
put(item)               向队列中放置数据，如果队列为满，则阻塞
get()                   从队列中取走数据，如果队列为空，则阻塞
join()                  如果队列不为空，则等待队列为空
task_done()             消费者从队列中取走一项数据，当队列变为空时，唤醒调用join()的线程
"""
from queue import Queue
from threading import Thread
import time


# 创建一个生产者类
class Producer(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(1, 6):
            print(f'{self.name}将产品{i}放入队列')
            self.queue.put(i)
            time.sleep(1)
        print('生产者完成了所有数据的存放')


# 创建一个消费者类
class Consumer(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for _ in range(5):
            value = self.queue.get()
            print(f'消费者线程：{self.name}取出了{value}')
            time.sleep(1)
        print('消费者线程完成了所有的数据的取出')


if __name__ == '__main__':
    # 创建队列
    queue = Queue()
    # 创建生产者
    p = Producer('Producer', queue)
    # 创建消费者
    c = Consumer('Consumer', queue)
    # 启动线程
    p.start()
    c.start()
    # 阻塞线程
    p.join()
    c.join()
    print('主线程执行结束')
