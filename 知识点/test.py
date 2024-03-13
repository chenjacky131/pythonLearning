import prettytable
table = prettytable.PrettyTable()
data = [
    ['第1行', '有票', '有票', '有票', '有票', '有票'],
    ['第2行', '有票', '有票', '有票', '有票', '有票'],
    ['第3行', '有票', '有票', '有票', '有票', '有票'],
    ['第4行', '有票', '有票', '有票', '有票', '有票'],
    ['第5行', '有票', '有票', '有票', '有票', '有票'],
    ['第6行', '有票', '有票', '有票', '有票', '有票']
]
table_head_data = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
table.field_names = table_head_data
table.clear_rows()
table.add_rows(data)
print(type(table.field_names))
