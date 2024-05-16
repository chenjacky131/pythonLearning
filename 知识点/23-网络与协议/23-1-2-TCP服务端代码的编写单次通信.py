"""
TCP服务器端流程如下：
1.使用socket类创建一个套接字对象
2.使用bind((ip, port))方法绑定IP地址和端口号
3.使用listen()方法开始TCP监听
4.使用accept()方法等待客户端的连接
5.使用recv()/send()方法接收/发送数据
6.使用close()关闭套接字
"""
from socket import socket, AF_INET, SOCK_STREAM
# AF_INET  用于Internet之间的进程通信
# SOCK_STREAM  表示的是用TCP协议编程
#  创建socket对象
server_socket = socket(AF_INET, SOCK_STREAM)
#  绑定IP地址和端口
ip = '127.0.0.1'  # 等同于localhost
port = 8888
server_socket.bind((ip, port))
server_socket.listen(5)  # 使用listen开始监听
print('服务器已启动')
client_socket, client_addr = server_socket.accept()  # 等待客户端的连接.系列解包赋值
data = client_socket.recv(1024)  # 接收来自客户端的数据
print('客户端发过来的数据为：', data.decode('utf-8'))  # 要求客户端发过来的数据是使用utf-8编码的
server_socket.close()   # 关闭socket
