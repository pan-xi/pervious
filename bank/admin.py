import time


class Admin(object):
    admin = "1"
    passwd = "1"

    # def __init__(self,admin):
    #     self.__admin=admin
    def printAdminView(self):
        print("********************************************")
        print("*                                          *")
        print("*                                          *")
        print("*                 欢迎登陆                         *")
        print("*                                          *")
        print("*                                          *")
        print("*                                          *")
        print("********************************************")


    def printsysFunctionView(self):
        print("********************************************")
        print("*     开户（1）           查询（2）        *")
        print("*     取款（3）           存款(4）         *")
        print("*     转账（5）           改密（6）        *")
        print("*     锁定（7）           解锁（8）        *")
        print("*     补卡（9）           销户（0）        *")
        print("*                退出（t）                 *")
        print("********************************************")

    def adminOption(self):
        inputAdmin = input("请输入管理员账号：")
        if self.admin != inputAdmin:
            print("账号输入错误")
            return -1
        inputPasswd = input("请输入密码")
        if self.passwd != inputPasswd:
            print("密码错误")
            return -1
        # 能执行到这里，账号密码正确
        print("操作成功！请稍候......")
        time.sleep(2)
        return 0
