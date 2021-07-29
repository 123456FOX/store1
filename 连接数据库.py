import pymysql
import random

# 连接数据库
con = pymysql.connect(host='localhost', user='root', password='root', database='bank')
# 创建控制台
cursor = con.cursor()
# 创建SQL语句
bank = {}
bank_name = '中国工商银行昌平回龙观昌平区'


# 2.打印界面显示
def welcome():
    print('************中国工商银行********** 您身边的银行  可信赖的银行')
    print('终端编号：123456')
    print('               请选择您要交易的类型                       ')
    print('                1.开户                                 ')
    print('                2.存款                                 ')
    print('                3.取款                                 ')
    print('                4.转账                                 ')
    print('                5.查询                                 ')
    print('                6.退出                                 ')
    print('*欢迎下次光临*'.center(50, '*'))


# 银行开户操作
def bank_adduser(only_count, username, password, country, province, street, room_number, money):
    cursor.execute("SELECT * from user")
    a = cursor.fetchall()
    if len(a) >= 100:
        return 3
    cursor.execute('select*from user where account=%s ' % only_count)
    f = cursor.fetchone()
    if f is not None:
        return 2
    else:
        # bank[only_count] = {
        #     'username': username,
        #     'password': password,
        #     'country': country,
        #     'province': province,
        #     "street": street,
        #     'room_number': room_number,
        #     'money': money,
        #     'bank_name': bank_name
        # }
        # print('开户成功')
        sql = 'insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        a = [only_count, username, password, country, province, street, room_number, money, bank_name]

        # 执行sql语句
        cursor.execute(sql, a)
        # 提交到数据库
        con.commit()
        return 1


# 银行的存款操作
def bank_deposit(only_count, save_money):
    cursor.execute('select*from user where account=%s' % only_count)
    g = cursor.fetchone()
    if g is None:
        return False
    else:
        # bank[only_count]['money'] = bank[only_count]['money'] + save_money
        sql = 'update user set money = money + %s where account = %s'
        b = [save_money, only_count]
        cursor.execute(sql, b)
        con.commit()


# 银行的取款操作
def bank_withdrawal(only_count, password, take_money):
    cursor.execute('select *from user where account=%s' % only_count)
    h = cursor.fetchone()
    if h is None:
        return 1
    elif password != h[2]:
        return 2
    elif take_money > h[7]:
        return 3
    else:
        sql = 'update user set money=money-%s where password=%s and account=%s'
        c = [take_money, password, only_count]
        cursor.execute(sql, c)
        con.commit()


# 银行的转账操作
def bank_transferAccounts(only_count, only_count1, password, transmoney):
    cursor.execute('select *from user where account=%s' % only_count)
    l = cursor.fetchone()
    cursor.execute('select *from user where account=%s' % only_count1)
    z = cursor.fetchone()
    if l is None:
        return 1
    elif z is None:
        return 1
    elif password != l[2]:
        return 2
    elif transmoney > l[7]:
        return 3
    else:
        # bank[only_count]['money'] = bank[only_count]['money'] - transmoney
        # bank[only_count1]['money'] = bank[only_count1]['money'] + transmoney
        sql = 'UPDATE user SET money=money-%s where account=%s and password=%s'
        sql1 = 'UPDATE user SET money=money+%s where account=%s'
        d = [transmoney, only_count, password]
        e = [transmoney, only_count1]
        cursor.execute(sql, d)
        cursor.execute(sql1, e)
        con.commit()


# 银行的查询操作
def bank_query(only_count, password):
    cursor.execute('select*from user where account=%s' % only_count)
    x = cursor.fetchone()
    if x is None:
        print('您要查询的用户不存在')
    else:
        if password != x[2]:
            print('密码错误')
        else:
            sql = 'select*from user where account=%s'
            e = [only_count]
            cursor.execute(sql, e)
            cursor.fetchone()
            con.commit()
            print('查询成功！')
            info = '''
            -----     个人账户信息明细     ------
                用户名: %s
                密码: %s
                地址信息
                    国家：%s
                    省份：%s
                    街道：%s
                    门牌号: %s
                余额：%s
                当前账户开户行：%s
            '''
            print(info % (x[1],
                          x[2],
                          x[3],
                          x[4],
                          x[5],
                          x[6],
                          x[7],
                          x[8])
                  )


# 用户开户操作
def adduser():
    username = input('请输入您的用户名:\n')
    while True:
        password = input('请输入您的密码:\n')
        if len(password) != 6:
            print("密码为6位数字")
        else:
            if password.isdigit():
                password = int(password)
                break
            else:
                print("输入非法")

    country = input('请输入您的国籍:')
    province = input('请输入您的省份:')
    street = input('请输入您的街道:')
    room_number = input('请输入您的门牌号:')
    money = int(input('请输入您的初始金额:'))
    only_count = random.randint(10000000, 99999999)
    status = bank_adduser(only_count, username, password, country, province, street, room_number, money)
    if status == 3:
        print('对不起，本银行已饱和')
    if status == 2:
        print('对不起，您的账户已存在')
    else:
        print('添加用户成功！')
        info = '''
                -----     个人账户信息明细     ------
                    用户名: %s
                    密码: %s
                    地址信息
                        国家：%s
                        省份：%s
                        街道：%s
                        门牌号: %s
                    余额：%s
                    账号：%s
                    账号开户行：%s
            '''
        print(info % (username, password, country, province, street, room_number, money, only_count, bank_name))


# 用户存款操作
def adddeposit():
    only_count = input('请输入您的账号:\n')
    if only_count.isdigit():
        only_count = int(only_count)
        save_money = input('请输入您要存储的金额:\n')
        save_money = int(save_money)
        status = bank_deposit(only_count, save_money)
        if status == False:
            print('您输入的账户不存在')
        else:
            cursor.execute("SELECT * FROM `user` where account = %s " % only_count)
            g = cursor.fetchone()
            print('存款成功！')
            info = '''
             -----     个人账户信息明细     ------
                    账号: %s
                    余额：%s




                    '''
            print(info % (g[0], g[7]))


# 用户的取钱操作
def addwithdrawal():
    only_count = input('请输入您的账号')
    if only_count.isdigit():
        only_count = int(only_count)
        password = int(input('请输入您的密码'))
        take_money = input('请输入您要取款的金额')
        take_money = int(take_money)
        status = bank_withdrawal(only_count, password, take_money)
        if status == 1:
            print('您的账号错误')
        elif status == 2:
            print('您的密码错误')
        elif status == 3:
            print('您的余额不足！')
        else:
            cursor.execute('select*from user where account=%s' % only_count)
            j = cursor.fetchone()
            print('取款成功！')
            # bank[only_count]['money'] = bank[only_count]['money'] - take_money
            info = '''
             -----     个人账户信息明细     ------
                        账号: %s
                        余额：%s
            '''
            print(info % (j[0], j[7]))


# 用户的转账操作
def transferAccounts():
    only_count = int(input('请输入您的账号'))
    password = int(input('请输入您的密码'))
    only_count1 = int(input('请输入对方账号'))
    transmoney = int(input('请输入转账金额'))
    status = bank_transferAccounts(only_count, only_count1, password, transmoney)
    if status == 1:
        print('您输入的账号错误')
    elif status == 2:
        print('您输入的密码错误')
    elif status == 3:
        print('您的账户余额不足')
    else:
        cursor.execute('select *from user where account=%s' % only_count)
        l = cursor.fetchone()
        cursor.execute('select *from user where account=%s' % only_count1)
        z = cursor.fetchone()
        print('转账成功')
        info = '''
            -----     个人账户信息明细     ------
                账号: %s
                对方账号：%s
                转账金额：%s
    '''
        print(info % (l[0], z[0], transmoney))


# 用户的查询
def query():
    only_count = int(input('请输入查询账号'))
    password = int(input('请输入账号密码'))
    bank_query(only_count, password)


while True:
    welcome()
    choose = input('请选择您要交易的类型:')
    if choose == "1":
        adduser()
    elif choose == '2':
        adddeposit()
    elif choose == '3':
        addwithdrawal()
    elif choose == '4':
        transferAccounts()
    elif choose == '5':
        query()
    elif choose == '6':
        print('期待与您再次相遇')
        break
    else:
        print("输入错误，请重新输入")
cursor.close()
con.close()
