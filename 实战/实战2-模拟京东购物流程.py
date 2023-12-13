"""
从键盘录入5个商品信息（1001手机）添加到商品列表中，展示商品信息，提示用户选择商品，
用户选中的商品添加到购物车中（购物车中的商品要逆序），用户选中的商品不存在需要有相
应的提示，当用户输入"q"时循环结束，显示购物车中的商品
"""
goods = []  # 商品列表
for i in range(1, 6):  # 循环录入商品
    _input = input('请输入商品的编号和商品的名称进行商品入库，每次只能输入一件商品：')
    goods.append(_input)
for item in goods:  # 输出商品列表
    print(item)
shoppingCart = []  # 购物车里的商品列表
while True:  # 循环选购商品
    goodsNotExistFlag = True  # 商品是否不存在的临时变量
    goodsId = input('请输入要购买的商品编号：')
    if goodsId == 'q':
        break
    for item in goods:
        if goodsId in item:
            shoppingCart.append(item)
            print('商品已成功添加到购物车')
            goodsNotExistFlag = False
            break
    if goodsNotExistFlag:
        print('该商品不存在！')
print('-' * 30)
print('您购物车里已选择的商品为：')
shoppingCart.reverse()
for item in shoppingCart:
    print(item)
