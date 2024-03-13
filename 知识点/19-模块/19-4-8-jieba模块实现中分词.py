"""
jieba是Python中用于对中文进行分词的模块，它可以将一段中文文本分隔
成中文词组的序列
"""
import jieba

# 读出进来
with open('华为笔记本.txt', 'r', encoding='utf-8') as file:
    s = file.read()
# print(s)
# 分词
lst = jieba.lcut(s)
# print(lst)
new_list = []
for item in lst:
    if len(item) >= 2:
        new_list.append(item)
# print(new_list)
dct = {}
for item in new_list:
    if item in dct:
        dct[item] = dct.get(item) + 1
    else:
        dct[item] = 1
# print(dct)
lst2 = []
for [key, value] in dct.items():
    lst2.append([key, value])
lst2.sort(key=lambda x: x[1], reverse=True)
print(lst2)
