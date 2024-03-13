"""
字符串的编码
    将str类型转换成bytes类型，需要使用到字符串的encode方法
    str.encode(encoding = 'utf-8', errors = 'strict/ignore/replace')
字符串的解码
    将bytes类型转换成str类型，需要使用到bytes类型的decode方法
    bytes.decode(encoding = 'utf-8', errors = 'strict/ignore/replace')
"""
s = '伟大的中国梦'
# 编码 str->bytes
encode_s = s.encode()
print(encode_s)  # 默认是utf-8，因为utf-8中文占3个字节
print(s.encode('gbk'))  # gbk中，中文占2个字节
# 编码中的出错问题
s2 = '耶✌'
encode_s2 = s2.encode('gbk', 'replace')
print(encode_s2)
# 解码 bytes->str
print(bytes.decode(encode_s))
print(bytes.decode(encode_s2, 'gbk'))
