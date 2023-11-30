# 标识符的命名规范和js一样，保留字严格区分大小写，允许用中文作为标识符，但是不建议使用。
import keyword  # 关键字模块

print(keyword.kwlist)
print(len(keyword.kwlist))  # 获取保留字的个数
