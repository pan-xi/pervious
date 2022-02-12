import socket

# 创建一个socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定ip端口   也是元组，尽量不要用1024以下的端口
server.bind(('192.168.60.113', 8080))
# 监听
server.listen(5)
print("服务器启动")
clientScoket, clientAddress = server.accept()
print("%s -- %s连接成功" % (str(clientScoket), clientAddress))
# 等待连接
while True:
    data = clientScoket.recv(1024)
    print("收到" + str(clientScoket) + "的数据" + data.decode("utf-8"))
    sendData=input("请输入返回给客户端的数据")
    clientScoket.send(sendData.encode("utf-8"))
