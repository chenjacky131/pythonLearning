"""
判断三个变量是否能构成一个三角形，如果不能则抛出异常Exception异常，
显示异常信息 “a、b、c不能构成三角形”，如果可以构成则显示三角形三个边长。
"""
try:
    border1 = int(input('请输入第一条边：'))
    border2 = int(input('请输入第二条边：'))
    border3 = int(input('请输入第三条边：'))
    if border1 + border2 > border3 \
            and border1 + border3 > border2 \
            and border2 + border3 > border1 \
            and border1 - border2 < border3 \
            and border1 - border3 < border2 \
            and border2 - border3 < border1:
        print(f'三角形的边长为：a={border1},b={border2},c={border3}')
    else:
        raise Exception(f'{border1},{border2},{border3}不能构成三角形')
except Exception as e:
    print(e)
