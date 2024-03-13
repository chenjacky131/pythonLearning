"""
json模块的常用函数
函数名称                        描述说明
json.dumps(obj)             将Python数据类型转成JSON格式过程，编码过程
json.loads(s)               将JSON格式字符转成Python数据类型，解码过程
json.dump(obj, file)        与dumps功能相同，将转换结果存储到文件file中
json.load(file)             与loads功能更相同，从文件file中读取数据
"""
import json
# 准备高维数据
lst = [
    {'name': '康康', 'age': 18, 'score': 90},
    {'name': '麦克', 'age': 21, 'score': 99},
    {'name': '玛丽亚', 'age': 19, 'score': 89}
]
s = json.dumps(lst, ensure_ascii=False, indent=4)  # ensure_ascii正常显示中文，indent数据缩进
print(type(s))  # 编码列表转成字符串
# 解码
lst2 = json.loads(s)
print(type(lst2))
# 编码到文件中
with open('student.txt', 'w') as file:
    json.dump(lst, file, ensure_ascii=False, indent=4)
# 解码到程序
with open('student.txt', 'r') as file:
    lst3 = json.load(file)
    print(type(lst3))
    print(lst3)
