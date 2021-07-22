# auThor : FOX
import random

# 1.银行仓库
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
def bank_adduser(username, password, country, province, street, room_number, money, only_count):
    if len(bank) >= 100:
        return 3
    if only_count in bank:
        return 2
    else:
        bank[only_count] = {
            'username': username,
            'password': password,
            'country': country,
            'province': province,
            "street": street,
            'room_number': room_number,
            'money': money
        }
        print('开户成功')
        return 1


# 银行的存款操作
def bank_deposit(only_count):
    if only_count not in bank:
        return False


# 银行的取款操作
def bank_withdrawal(only_count, password, take_money):
    if only_count not in bank:
        return 1
    if password != bank[only_count]['password']:
        return 2
    if take_money > bank[only_count]['money']:
        return 3


# 银行的转账操作
def bank_transferAccounts(only_count, only_count1, password, transmoney):
    if only_count not in bank:
        return 1
    if only_count1 not in bank:
        return 1
    if password != bank[only_count]['password']:
        return 2
    if transmoney > bank[only_count]['money']:
        return 3


# 银行的查询操作
def bank_query(only_count, password):
    if only_count not in bank:
        print('您要查询的用户不存在')
    else:
        if password != bank[only_count]['password']:
            print('密码错误')
        else:
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
            print(info % (bank[only_count]['username'],
                          bank[only_count]['password'],
                          bank[only_count]['country'],
                          bank[only_count]['province'],
                          bank[only_count]['street'],
                          bank[only_count]['room_number'],
                          bank[only_count]['money'],
                          bank_name)
                  )


# 用户的开户操作
def adduser():
    # global bank
    username = input('请输入的用户名:')
    while True:
        password = input('请输入您的密码:')
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
    status = bank_adduser(username, password, country, province, street, room_number, money, only_count)
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
        '''
        print(info % (username, password, country, province, street, room_number, money, only_count))


# 用户存款操作
def adddeposit():
    only_count = input('请输入您的账号')
    if only_count.isdigit():
        only_count = int(only_count)
        money = input('请输入您要存储的金额')
        money = int(money)
        status = bank_deposit(only_count)
        if status == False:
            print('您输入的账户不存在')
        else:
            print('存款成功！')
            info = '''
             -----     个人账户信息明细     ------
                    账号: %s
                    余额：%s
                          
                    
                    
                    
                    '''
            print(info % (only_count, money))


# 用户的取钱操作
def addwithdrawal():
    only_count = input('请输入您的账号')
    if only_count.isdigit():
        only_count = int(only_count)
        password = input('请输入您的密码')
        take_money = input('请输入您要取款的金额')
        take_money = int(take_money)
        status = bank_withdrawal(only_count, password, take_money)
        if status == 1:
            print('您的账号错误')
        if status == 2:
            print('您的密码错误')
        if status == 3:
            print('您的余额不足！')
        else:
            print('取款成功！')
            bank[only_count]['money'] = bank[only_count]['money'] - take_money
    info = '''
     -----     个人账户信息明细     ------
                账号: %s
                余额：%s
    '''
    print(info % (only_count, bank[only_count]['money']))


# 用户的转账操作
def transferAccounts():
    only_count = int(input('请输入您的账号'))
    password = input('请输入您的密码')
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
        print('转账成功')
        info = '''
            -----     个人账户信息明细     ------
                账号: %s
                对方账号：%s
                转账金额：%s
    '''
        print(info % (only_count, only_count1, transmoney))


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
