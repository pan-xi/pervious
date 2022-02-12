import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('192.168.60.113',8080))

count=0
while True:
    count+=1
    data=input("请输入给服务器发送到数据")
    client.send(data.encode("utf-8"))#一定要编码因为不能直接传输str
    info=client.recv(1024)#接收服务器数据
    print("服务器说："+info.decode("utf-8"))#一定要编码因为传来是bytes


