"""
从键盘录入5位好友的姓名和电话，由于通讯录是无序的，
所以可以使用集合来实现
"""
set_contact = set()  # 创建通讯录集合
for i in range(1, 6):
    contact = input('请输入第' + str(i) + '位好友的姓名和手机号码：')
    set_contact.add(contact)
for item in set_contact:
    print(item)
