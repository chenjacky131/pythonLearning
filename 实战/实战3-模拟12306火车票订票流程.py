"""
假设北京到天津有以下4个车次可供选择，用户选择索要购买的车次，
进行购票进站。
"""
dict_ticket = {
    'G1569': ['北京南-天津南', '18:06', '18:39', '00:33'],
    'G1567': ['北京南-天津南', '18:15', '18:49', '00:34'],
    'G8917': ['北京南-天津西', '18:20', '19:19', '00:59'],
    'G203': ['北京南-天津南', '18:35', '19:09', '00:34']
}
lst = ['车次  ', '出发站-到达站', '出发时间', '到达时间', '历史时长']
for item in lst:
    print(item, end='\t\t')
print()
for key, item in dict_ticket.items():
    print(key, end='\t\t')
    for sub_item in item:
        print(sub_item, end='\t\t')
    print()
trainNum = input('请输入要购票的车次：')
if not dict_ticket.get(trainNum):
    print('车次不存在！')
else:
    passengers = input('请输入乘车人，如果是多位乘车人使用逗号分隔：')
    for key, item in dict_ticket.items():
        value = dict_ticket.get(key)
        _address = value[0]
        _departTime = value[1]
        if trainNum == key:
            print('您已购买了', key, ' ', _address, ' ', _departTime, '开,请', passengers, '尽快换取纸质车票。【铁路客服】')
            break
