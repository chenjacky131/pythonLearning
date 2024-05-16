"""
TCP客户端的流程如下：
1.使用socket类创建一个套接字对象
2.使用connect((host, port))设置连接的主机IP和主机设置的端口号
3.使用recv()/send()方法接收/发送数据
4.使用close()关闭套接字
代码在client里面的客户端的代码编写单次通信
"""
import socket
client_socket = socket.socket()
# IP地址和主机端口
ip = '127.0.0.1'
port = 8888
client_socket.connect((ip, port))
print('与服务器连接建立成功')
# 发送数据
client_socket.send('Welcome to python world'.encode('utf-8'))
# 关闭
client_socket.close()
print('发送完毕')
