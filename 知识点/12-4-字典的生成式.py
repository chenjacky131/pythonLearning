"""
d = {key:value for item in range}
d = { key: value for key, value in zip(lst1, lis2)}
"""
import random

d = {item: random.randint(1, 100) for item in range(4)}
print(d)

lst1 = [100, 200, 300]
lst2 = ['jack', 'bruce', 'harry']
d = {key: value for key,value in zip(lst1, lst2)}
print(d)
