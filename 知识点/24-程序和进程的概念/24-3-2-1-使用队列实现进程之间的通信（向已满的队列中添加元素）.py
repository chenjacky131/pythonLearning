from multiprocessing import Queue

if __name__ == '__main__':
    q = Queue(3)
    # 向队列中添加元素读（入队）
    q.put('hello')  # block=True
    q.put('world')
    q.put('Python')

    q.put('html')  # 一直等待，因为队列已满
