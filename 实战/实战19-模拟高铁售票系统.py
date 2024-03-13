"""
假设高铁一节车厢的座位数有6行，每行5列，每个座位初始显示“有票”，
用户输入座位位置（如，4，3）后，按回车，则该位置显示为“已售”，使用
到第三方模块prettytable
"""
import prettytable


class TicketSellingSystem:  # 高铁售票系统类
    def __init__(self, row_num, column_num):
        self.row_num = row_num  # 座位行数
        self.column_num = column_num  # 座位列数
        self.table = prettytable.PrettyTable()  # 展示表格属性
        self.exit = False  # 退出订票流程
        self.table_data = []
        self.gen_table_head()
        self.gen_table_body()
        print(self.table)
        self.start_order_ticket()

    def gen_table_head(self):  # 生成表头
        arr = []
        for n in range(0, self.column_num + 1):  # 添加表头
            arr.append('行号' if n == 0 else f'座位{n}')
        self.table.field_names = arr  # 不能直接append数据到field_names里，会报错

    def gen_table_body(self):  # 生成表格
        if len(self.table_data) == 0:
            for r in range(0, self.row_num):
                row_data = []
                for c in range(0, self.column_num + 1):
                    if c == 0:
                        row_data.append(f"第{r+1}行")
                    else:
                        row_data.append("有票")
                self.table_data.append(row_data)
        self.table.clear_rows()

        self.table.add_rows(self.table_data)

    def start_order_ticket(self):  # 开始订票
        while self.exit is not True:
            seat_num = input('请输入选择的坐席。如4,3表示第4排第3列：')
            if seat_num == 'exit':
                self.exit = True
            else:
                [r_n, c_n] = seat_num.split(',')  # 获取输入参数
                cell_data = self.table_data[int(r_n) - 1][int(c_n)]
                if cell_data == '有票':
                    self.table_data[int(r_n) - 1][int(c_n)] = '已售'
                    print(f'您已购买{r_n}排{c_n}列的座位，路途愉快！')
                    self.gen_table_body()
                else:
                    print(f'该位置({r_n},{c_n})已售，请重新选择座位。')
                print(self.table)


ticketSystem = TicketSellingSystem(6, 5)
