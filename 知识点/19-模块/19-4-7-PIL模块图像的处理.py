"""
PIL是用于图像处理的第三方库，它支持图像存储、处理和显示等操作
"""
from PIL import Image
#  加载图片
im = Image.open('pic.jpg')
# print(im, type(im))
#  提取RGB图像的颜色通道，返回结果是图像的副本
r, g, b = im.split()
# print(r, g, b)
#  合并通道
om = Image.merge(mode='RGB', bands=(r, g, b))
om.save('new_pic.jpg')
