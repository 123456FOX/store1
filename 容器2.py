"""
    需求：
        购物流程。
        1.商品在货架上
        2.空的购物车
        3.自己的初始化资金
    技术选型：
        1.容器
            列表： []
        2.循环技术
            while
            for i in  enumerate(li)
        3.判断
        4.键盘输入
    任务：
        [10张老干妈：7折优惠券，20张联想电脑1折优惠券]
        开始买东西之前，提示是否要抽一张优惠券。
            若是：随机给一张，最终要进行使用优惠券的进行结算。
            若否：正常买东西
"""
# 商品列表
import random

shop = [
    ['手表', 200],
    ['联想', 100],
    ['猪猪侠', 600],
    ['烤乳猪', 2000],
    ['老干妈', 9]
]
# 空的购物车
myCar = []

# 初始资金
money = input('初始金额:\n')
money = int(money)

# 打折后的购物车
shop1 = [
    ['手表', 200],
    ['联想', 10],
    ['猪猪侠', 600],
    ['烤乳猪', 2000],
    ['老干妈', 6.3]
]


# 优惠券
coupon = random.randint(1, 30)
extract = input('是否需要优惠券 需要y,不需要n\n')
while True:
    if extract == 'y':
        if coupon <= 10:
            print('获得老干妈优惠券一张')
        else:
            print('获得联想优惠券一张')
        break
    elif extract == 'n':
        print('原价购物')
        break
    else:
        print('请重新输入')
while True:
    for key, value in enumerate(shop):
        print(key, value)
    choose = input('输入商品编号')
    if choose.isdigit():
        choose = int(choose)
        if choose > 4:
            print('没有此商品')
        else:
            if extract == 'y':
                if money >= shop[choose][1] * 0.1 and choose == 1 and coupon > 10:
                    myCar.append(shop[choose])
                    money = money - shop[choose][1] * 0.1
                    print('购买成功', '余额为', money, '￥')
                elif money >= shop[choose][1] and choose == 4 and coupon <= 10:
                    myCar.append(shop[choose])
                    money = money - shop[choose][1]
                    print('购买成功', '余额为', money, '￥')
                elif money > shop[choose][1]:
                    myCar.append(shop[choose])
                    money = money - shop[choose][1]
                    print('购买成功', '余额为', money, '￥')
                else:
                    print('出门左拐')

            elif extract == 'n':
                if money >= shop[choose][1]:
                    myCar.append(shop[choose])
                    money = money - shop[choose][1]
                    print('购买成功', '余额为', money, '￥')
                else:
                    print('出门右拐')

    elif choose == 'q' or 'Q':
        print('再见！')
        break
    else:
        print('输入正确编号')
print('购物清单')
for key, value in enumerate(myCar):
    print(key, value)
print('余额',money)