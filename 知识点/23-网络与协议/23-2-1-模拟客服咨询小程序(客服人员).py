from socket import socket, AF_INET, SOCK_DGRAM
# 创建socket
recv_socket = socket(AF_INET, SOCK_DGRAM)
# 绑定IP地址和端口
recv_socket.bind(('127.0.0.1', 8888))
while True:
    #  接收方发送过来的数据
    recv_data, addr = recv_socket.recvfrom(1024)
    print('客户说：', recv_data.decode('utf-8'))
    if recv_data.decode('utf-8') == 'bye':
        break
    # 准备回复对方的数据
    data = input('客服回：')
    # 发送
    recv_socket.sendto(data.encode('utf-8'), addr)
# 关闭socket对象
recv_socket.close()
