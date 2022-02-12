import tkinter
import socket
import threading
win = tkinter.Tk()
win.title("qq服务器")
win.geometry("400x400+200+0")
users={}
def run(cs,ca):
    print("**********")
    userName = cs.recv(1024)
    users[userName.decode("utf-8")]=cs
    print(users)

    while True:
        rData=cs.recv(1024)
        dataStr=rData.decode("utf-8")
        infoList=dataStr.split(":")
        users[infoList[0]].send((userName.decode("utf-8")+"说："+infoList[1]).encode("utf-8"))


def start():
    ipStr = eip.get()
    portStr = eport.get()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ipStr, int(portStr)))
    server.listen(5)
    printStr="服务器启动成功"
    text.insert(tkinter.INSERT, printStr)
    while True:
        cs, ca = server.accept()
        # print("%s -- %s连接成功" % (str(clientScoket), clientAddress))
        t = threading.Thread(target=run, args=(cs, ca))
        t.start()

def startServer():
    s=threading.Thread(target=start)
    s.start()



labelIP = tkinter.Label(win, text="IP").grid(row=0, column=0)
labelPort = tkinter.Label(win, text="labelPort").grid(row=1, column=0)
eip = tkinter.Variable()
eport = tkinter.Variable()
entryIP = tkinter.Entry(win, textvariable=eip).grid(row=0, column=1)
entryPort = tkinter.Entry(win, textvariable=eport).grid(row=1, column=1)
button = tkinter.Button(win, text="启动", command=startServer).grid(row=2, column=0)
text = tkinter.Text(win, width=30, height=10)
text.grid(row=3, column=0)





win.mainloop()
