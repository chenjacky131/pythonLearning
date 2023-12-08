"""
列表的排序可以用列表对象的sort方法，也可以使用内部函数sorted
lst.sort(key=None, reverse=False)
sorted(lst,key=None, reverse=False
key表示排序规则，reverse表示排序方式（默认升序）
key=str.lower先转成小写再排序
"""
lst = ['apple', 'banana', 'pear', 'Orange']
lst.sort(key=str.upper)
print(lst)
