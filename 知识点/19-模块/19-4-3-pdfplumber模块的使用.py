"""
pdfplumber可用于从PDF文件中读取内容
"""
import pdfplumber
# 打开pdf文件
with pdfplumber.open('vpn.pdf') as pdf:
    for i in pdf.pages:  # 遍历页
        print(i.extract_text())  # 提取内容
        print(f'---------{i.page_number}页结束----------')
