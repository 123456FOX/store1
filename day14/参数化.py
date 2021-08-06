from unittest import TestCase
from ddt import*
from bank import Bank

# 数据源
add = [
    [1, 1, 111111, 1, 1, 1, 1, 1000],
    [2, 1, 111111, 1, 1, 1, 1, 1000]
]
save = [
    [1, 100]
]
get = [
    [1, 111111, 100]  # account, pwd, money
]
query = [
    [1, 111111]  # account, pwd
]

transfer = [
    [1, 2, 111111, 100]  # account, account1, pwd, transferMon
]

@ddt
class TestBank(TestCase):
    # 测试开户
    @data(*add)
    @unpack
    def testaddUser(self, account, username, password, country, province, street, gate, money):
        bank = Bank()
        bank.bank_addUser(account, username, password, country, province, street, gate, money,)

    # 测试存钱
    @data(*save)
    @unpack
    def testsaveMoney(self, account, money):
        bank = Bank()
        bank.bank_saveMoney(account, money)

    # 测试取钱
    @data(*get)
    @unpack
    def testgetMoney(self, account, pwd, money):
        bank = Bank()
        bank.bank_drawMoney(account, pwd, money)

    # 测试查询
    @data(*query)
    @unpack
    def testquery(self, account, pwd):
        bank = Bank()
        bank.bank_userQuery(account, pwd)

    @data(*transfer)
    @unpack
    def testtransferMoney(self, account, account1, pwd, transferMon):
        bank = Bank()
        bank.bank_transferMoney(account, account1, pwd, transferMon)
