"""
使用python第三方库jieba与wordcloud实现对华为笔记本评论的词云图
"""
import jieba
from wordcloud import WordCloud
# 读取数据
with open('华为笔记本.txt', 'r', encoding='utf-8') as file:
    s = file.read()
# 中文分词
lst = jieba.lcut(s)
txt = ''.join(lst)
# 绘制词云图
wc = WordCloud(background_color='white', font_path='AlimamaDaoLiTi.ttf')
# 由文本生成词云图
wc.generate(txt)
# 保存图片
wc.to_file('评价词云图.png')
