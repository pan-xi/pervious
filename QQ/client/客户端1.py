import tkinter
import socket
import threading
win = tkinter.Tk()
win.title("joe")
win.geometry("400x400+200+0")
cs=None
def getInfo():
    while True:
        data=cs.recv(1024)
        text.insert(tkinter.INSERT,data.decode("utf-8"))

def connectServer():
    ipStr=eip.get()
    portStr=eport.get()
    userStr=euser.get()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ipStr, int(portStr)))
    client.send(userStr.encode("utf-8"))#一定要编码因为不能直接传输str
    global cs
    cs=client
    #等待接收数据
    t=threading.Thread(target=getInfo)
    t.start()

def sendmsg():
    friend=efriend.get()
    sendStr=esend.get()
    sendStr=friend+":"+sendStr
    cs.send(sendStr.encode("utf-8"))


labelUser = tkinter.Label(win, text="userName").grid(row=0, column=0)
euser = tkinter.Variable()
entryUser = tkinter.Entry(win, textvariable=euser).grid(row=0, column=1)
labelIP = tkinter.Label(win, text="ip").grid(row=1, column=0)
eip = tkinter.Variable()
entryIP = tkinter.Entry(win, textvariable=eip).grid(row=1, column=1)
labelPort = tkinter.Label(win, text="port").grid(row=2, column=0)
eport= tkinter.Variable()
entryPort = tkinter.Entry(win, textvariable=eport).grid(row=2, column=1)
button = tkinter.Button(win, text="链接", command=connectServer).grid(row=3, column=0)
text = tkinter.Text(win, width=30, height=5)
text.grid(row=4, column=0)
esend= tkinter.Variable()
entrySend = tkinter.Entry(win, textvariable=esend).grid(row=5, column=0)
efriend= tkinter.Variable()
entryFriend = tkinter.Entry(win, textvariable=efriend).grid(row=6, column=0)
button2 = tkinter.Button(win, text="发送", command=sendmsg).grid(row=7, column=0)


win.mainloop()