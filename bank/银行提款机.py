from admin import Admin
from ATM import ATM
import time
import pickle
import os


def main():  # 代替bank不写把bank类了
    #管理员开机
    adimn = Admin()  # 管理员对象
    adimn.printAdminView()
    if adimn.adminOption():  # 若返回-1则开机出错停止
        return -1
    #读文件信息
    absPath = os.getcwd()  # 获取当前目录绝对路径，避免文件夹移动bug
    filePath = os.path.join(absPath, "allUsers.txt")#得先创建这个txt要不然程序找不到会报错
    with open(filePath,"rb") as f:#读文件
        allUsers=pickle.load(f)#文件应该先写入一个，否则空文件电脑找不到东西会报错EOFError: Ran out of input
    #allUsers={}#第一次使用要先开一个户然后再进行上面的读取文件，如果没有开户则allUsers里面什么也没有会报错
    atm=ATM(allUsers)

    while True:
        # 等待用户操作
        adimn.printsysFunctionView()
        option = input("请输入您的操作：")
        if option == "1":
            atm.creatUser()
        elif option == "2":
            atm.searchUserInfo()
        elif option == "3":
            atm.getMoney()
        elif option == "4":
            print("存储")
        elif option == "5":
            print("转账")
        elif option == "6":
            print("改密")
        elif option == "7":
            atm.lockUser()
        elif option == "8":
            atm.unlockUser()
        elif option == "9":
            print("补卡")
        elif option == "0":
            print("销户")
        elif option == "t":
            if not adimn.adminOption():  # 用管理员登录关机如果返回0则不会走这里所以要加一个not

            #退出系统时保留用户信息到文件中

                with open(filePath,"wb") as f:
                    pickle.dump(atm.allUsers,f)
                return 0  # 0为正常，-1为出错







        time.sleep(2)


if __name__ == "__main__":
    main()
