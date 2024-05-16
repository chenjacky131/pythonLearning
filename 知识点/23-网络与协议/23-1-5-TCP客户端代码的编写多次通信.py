"""

"""
import socket
# 创建socket对象
client_socket = socket.socket()
# 绑定主机IP和端口号
client_socket.connect(('127.0.0.1', 8888))
print('已建立服务器连接')
# 客户端先发送数据
info = ''
while info != 'bye':
    # 准备发送的数据
    send_data = input('请客户端输入要发送的数据：')
    client_socket.send(send_data.encode('utf-8'))
    # 判断
    if send_data == 'bye':
        break   # 退出循环
    # 接收一条数据
    info = client_socket.recv(1024).decode('utf-8')
    print('收到服务器的响应数据：', info)
# 关闭socket对象
client_socket.close()
