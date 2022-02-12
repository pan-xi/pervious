from card import Card
from user import User
import random


class ATM(object):
    def __init__(self, allUsers):
        self.allUsers = allUsers  # （卡号，用户）

    # 创建用户
    def creatUser(self):  # 创建用户
        # 目标： 向字典中加入键值对（卡号，用户）
        name = input("请输入您的名字：")
        idCard = input("请输入身份证号：")
        phone = input("请输入电话号码：")
        prestoreMoney = int(input("请输入预存款："))
        if prestoreMoney <= 0:
            print("输入预存款有误！开户失败......")
            return -1
        onePasswd = input("请设置密码")
        if not self.checkPasswd(onePasswd):
            print("密码输入错误！开户失败.......")
            return -1
        # 到此为止需要用户输入的信息就完了
        cardStr = self.randomCardId()  # dict的key
        card = Card(cardStr, onePasswd, prestoreMoney)
        user = User(name, idCard, phone, card)
        self.allUsers[cardStr] = user  # 存到字典
        print("开户成功！请牢记卡号%s......." % (cardStr))

    # 查询用户
    def searchUserInfo(self):
        cardNumber = input("请输入卡号:")
        user = self.allUsers.get(cardNumber)  # user得到的是用户名因为get取得是value
        if not user:
            print("该卡号不存在！查询失败......")
            return -1
        if user.card.cardLock:
            print("该卡已被锁定！请解锁后再进行其他操作.....")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):  # user.card.cardpasswd存的是上面card实例化时传入的onepasswd
            print("密码输入错误!该卡已被锁定！请解锁后再进行其他操作.....")
            user.card.cardLock = True
            return -1
        print("账号：%s 余额：%d" % (user.card.cardId, user.card.cardMoney))

    # 取钱
    def getMoney(self):
        cardNumber = input("请输入卡号:")
        user = self.allUsers.get(cardNumber)  # user得到的是用户名因为get取得是value
        if not user:
            print("该卡号不存在！取钱失败......")
            return -1
        if user.card.cardLock:
            print("该卡已被锁定！请解锁后再进行其他操作.....")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):  # user.card.cardpasswd存的是上面card实例化时传入的onepasswd
            print("密码输入错误!该卡已被锁定！请解锁后再进行其他操作.....")
            user.card.cardLock = True
            return -1
        money = int(input("请输入取款金额："))  # 记得加int否则下面没办法比较
        if money > user.card.cardMoney:
            print("余额不足！取款失败.......")
            return -1
        if money <= 0:
            print("输入错误！取款失败.......")
            return -1
        user.card.cardMoney -= money
        print("取款成功！余额：%d" % (user.card.cardMoney))

    def saveMoner(self):
        pass

    def transferMoney(self):
        pass

    def changePasswd(self):
        pass

    # 锁定用户
    def lockUser(self):
        cardNumber = input("请输入卡号:")
        user = self.allUsers.get(cardNumber)  # user得到的是用户名因为get取得是value
        if not user:
            print("该卡号不存在！锁定失败......")
            return -1
        if user.card.cardLock:
            print("该卡已被锁定！请解锁后再使用其他功能.......")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):  # user.card.cardpasswd存的是上面card实例化时传入的onepasswd
            print("密码输入错误!该卡已被锁定！请解锁后再进行其他操作.....")
            user.card.card.cardLock = True
            return -1
        tempIdCard = input("请输入身份证号：")
        if tempIdCard != user.idCard:
            print("身份证输入错误！锁定失败......")
            return -1
        user.card.cardLock = True
        print("锁定成功")

    # 解锁用户
    def unlockUser(self):
        cardNumber = input("请输入卡号:")
        user = self.allUsers.get(cardNumber)  # user得到的是用户名因为get取得是value
        if not user:
            print("该卡号不存在！解锁失败......")
            return -1
        if not user.card.cardLock:
            print("该卡没有锁定！无需解锁.....")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):  # user.card.cardpasswd存的是上面card实例化时传入的onepasswd
            print("密码输入错误!解锁失败！请解锁后再进行其他操作.....")
            user.card.card.cardLock = True
            return -1
        tempIdCard = input("请输入身份证号：")
        if tempIdCard != user.idCard:
            print("身份证输入错误！解锁失败......")
            return -1
        user.card.cardLock = False
        print("解锁成功！")

    def newCard(self):
        pass

    def killUser(self):
        pass

    # 检查密码
    def checkPasswd(self, realPasswd):
        for i in range(3):
            tempPasswd = input("请输入密码:")
            if tempPasswd == realPasswd:
                return True
        return False

    # 生成卡号
    def randomCardId(self):
        while True:
            str1 = ""  # 必须用str1因为下面有一个str方法如果再定义一个str会冲突，在下面掉用的时候会使系统找不到方法
            for i in range(6):
                ch = str(random.randrange(0, 10))
                str1 += ch
            if not self.allUsers.get(str1):  # 判断是否重复不重复return str
                return str1
