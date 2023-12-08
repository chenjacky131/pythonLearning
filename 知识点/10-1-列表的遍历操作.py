lst = ['java', 'php', 'python']
# 使用遍历循环for遍历列表元素
for i in lst:
    print(i)
print('-' * 30)
# 使用for循环，range函数，len函数，根据索引进行遍历
for i in range(0, len(lst)):
    print(lst[i])
print('-' * 30)
# enumerate函数遍历,第二个参数为序号起始值,start单词可省略
for index, item in enumerate(lst, start=1):
    print('index:', index, '\titem:', item)
