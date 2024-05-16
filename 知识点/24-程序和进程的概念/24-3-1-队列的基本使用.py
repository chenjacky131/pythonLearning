"""
进程之间可以通过队列进行通信，队列是一种先进先出的数据结构。
创建队列的语法结构：
    队列对象 = Queue(N)
队列的基本方法
    方法名称                        功能描述
qsize()                     获取当前队列包含的消息数量
empty()                     判断队列是否为空，为空结果为True，否则为False
full()                      判断队列是否满了，满了为True，否则为False
get(block=True)             获取队列中的一条消息，然后从队列中移除，block默认值为True
get_nowait()                相当于get(block=False)，消息队列为空时，抛出异常
put(item, block=True)       将item消息放入队列，block默认为True
put_nowait(item)            相当于put(item, block=False)

"""
from multiprocessing import Queue

if __name__ == '__main__':
    # 创建一个队列
    q = Queue(3)  # 对多可以接收3条消息
    print('队列是否为空：', q.empty())
    print('队列是否为满：', q.full())
    print('-' * 10)
    # 向队列中添加消息
    q.put('hello')
    q.put('world')
    print('队列是否为空：', q.empty())
    print('队列是否为满：', q.full())
    print('-' * 10)
    q.put('Python')
    print('队列是否为空：', q.empty())
    print('队列是否为满：', q.full())
    print('-' * 10)
    print('队列中消息的个数：', q.qsize())
    # 出队
    print(q.get())
    print('队列中消息的个数：', q.qsize()) # 2
    # 入队
    q.put_nowait('html')
    # q.put_nowait('sql') # queue.Full
    # q.put('sql') # 不报错，会一直等待等到队列中有空位置
    # 遍历
    if not q.empty():
        for i in range(q.qsize()):
            print(q.get_nowait()) # nowait()不等待
    print('队列是否为空：', q.empty())
    print('队列是否为满：', q.full())
    print('队列中的消息个数：', q.qsize())
