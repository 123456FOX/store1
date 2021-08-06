import random
import time

import pymysql

# 准备一个数据库和银行名称
# 1.连接数据库
con = pymysql.connect(host="localhost", user="root", password="root", database="公安系统")

# 2.创建控制台
cursor = con.cursor()

# 银行名称
bank_name = "中国工商银行昌平回龙观支行"  # 银行名称写死的


# # 入口程序
# def welcome():
#     print("*************************************")
#     print("*      中国工商银行昌平支行            *")
#     print("*************************************")
#     print("*  1.开户                            *")
#     print("*  2.存钱                            *")
#     print("*  3.取钱                            *")
#     print("*  4.转账                            *")
#     print("*  5.查询                            *")
#     print("*  6.Bye！                           *")
#     print("**************************************")


# 银行的开户逻辑
class Bank:

    def bank_addUser(self,account, username, password, country, province, street, gate, money):
        # 1.判断数据库是否已满
        cursor.execute("SELECT * from user")
        record = cursor.fetchall()
        if len(record) >= 100:
            return 3
        else:
            # 2.判断用户是否存在
            cursor.execute("SELECT * from user where account = %s" % account)
            record1 = cursor.fetchone()
            if record1 is not None:
                return 2
            else:
                # 3.正常开户
                sql = "insert into  user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                a = [account, username, password, country, province, street, gate, money, bank_name]
                cursor.execute(sql, a)
                con.commit()
                return 1

    # 银行的存钱逻辑
    def bank_saveMoney(self,account, sm):
        cursor.execute("SELECT account FROM `user` where account = %s " % account)
        record = cursor.fetchone()
        # 判断是否存在数据库中
        if record is None:
            return False
        else:
            sql = "UPDATE `user` SET money=money+%s WHERE account=%s "
            data = [sm, account]
            cursor.execute(sql, data)  # (模板, 参数)
            con.commit()

    # 银行的取钱逻辑
    def bank_drawMoney(self,account, pwd, dm):
        # 判断账户是否在字典中
        cursor.execute("SELECT * FROM `user` where account = %s" % account)
        record = cursor.fetchone()
        if record is None:
            return 1
        if record[2] != pwd:
            return 2
        if record[7] < dm:
            return 3
        sql = "UPDATE `user` SET money = money - %s WHERE account = %s"
        data = [dm, account]
        cursor.execute(sql, data)
        con.commit()

    # 银行的转账逻辑
    def bank_transferMoney(self,account, intoAccount, pwd, tm):
        cursor.execute("SELECT * FROM `user` where account = %s" % account)
        record = cursor.fetchone()
        # 判断账户是否在数据库中
        if record is None:
            return 1
        # 判断转出账户密码的对错
        elif record[2] != pwd:
            return 2
        # 判断转账金额大于转出账户的余额
        elif record[7] < tm:
            return 3
        else:
            sql = "UPDATE `user` SET money=money-%s WHERE account=%s "
            sql1 = "UPDATE `user` SET money=money+%s WHERE account=%s "
            data = [tm, account]
            data1 = [tm, intoAccount]
            cursor.execute(sql, data)
            cursor.execute(sql1, data1)
            con.commit()

    # 银行的查询逻辑
    def bank_userQuery(self,account, pwd):
        cursor.execute("SELECT * FROM `user` where account = %s" % account)
        record = cursor.fetchone()

        if record is None:
            print('您输入的账号不存在！')
        else:
            if record[2] != pwd:
                print('您输入的密码不正确！')
            else:
                sql = "SELECT * FROM `user` WHERE account=%s AND `password`=%s"
                data = [account, pwd]
                cursor.execute(sql, data)  # (模板, 参数)
                con.commit()
                # print('查询成功，您的个人信息如下:')
                # info = '''
                #             ----------个人信息----------
                #             用户名：%s
                #             密码：%s
                #             账号：%s
                #             地址信息
                #                 国家：%s
                #                 省份：%s
                #                 街道：%s
                #                 门牌号: %s
                #             余额：%s
                #             开户行地址：%s
                #
                #             ---------------------------
                #         '''
                # print(info % (record[1], record[2], record[0], record[3], record[4], record[5], record[6], record[7],
                #               record[8]))
