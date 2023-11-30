"""
根据父母升高预测儿子身高。计算公式：儿子身高=（父亲身高+母亲身高）*0.54
"""
motherHeight = eval(input('请输入母亲身高：'))
fatherHeight = eval(input('请输入父亲身高：'))
print('预测儿子的身高为：', (motherHeight + fatherHeight) * 0.54)
