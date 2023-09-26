# 多次赋值后，变量名会指向新的空间
name = '玛丽亚'
print(name)
print('标识', id(name))
print('类型', type(name))
print('值', name)
