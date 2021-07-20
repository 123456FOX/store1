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

# # 初始资金
# money = input('初始金额:\n')
# money = int(money)

# 打折后的购物车
shop1 = [
    ['手表', 200],
    ['联想', 10],
    ['猪猪侠', 600],
    ['烤乳猪', 2000],
    ['老干妈', 6.3]
]


def hh():
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


def heihei():
    global money
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

                else:
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
    print('余额', money)


journey = {
    '梦幻小镇': {
        '乌拉那拉黑暗之神': {
            '北极圈': ['榴莲的家', '汉堡的家', '可乐的家'],
            '圣诞老人村': ['丹丹的家', '彤彤的家', '王锐的家'],
            '猪猪侠镇': ['夏云鹏的家', '刘锦克的家', '纪博文的家'],
            '青青草原': ['明慧的家', '大神的家']
        }
    },
    '希望小镇': {
        '格格巫': {
            '蓝精灵': ['懒洋洋的家', '美羊羊的家'],
            '呼啦圈': ['迪迦奥特曼的家', '赛文奥特曼的家'],
            '大耳朵图图的家': ['大头儿子的家', '海绵宝宝'],
            '中华小子': ['名侦探柯南的家', '蜡笔小新的家', '小宋当家'],
            '一休哥': ['超级无敌美少女的家', '风云的家', '天下第一的家']
        },
        '荔枝的家': {
            '无花果的家': ['桂圆的家', '花生的家'],
            '花生米的家': ['啤酒的家', '烤鸭的家']
        }
    }
}


def place(journey):
    for i in journey:
        print(i)


for i in journey:
    print(i)

while True:
    home1 = input('请输入要去的豪华套房\n')
    if home1 in journey:
        place(journey[home1])
        home2 = input('请输入要去的总统套房\n')
        if home2 in journey[home1]:
            place(journey[home1][home2])
            home3 = input('请输入要去的别墅\n')
            if home3 in journey[home1][home2]:
                place(journey[home1][home2][home3])
                shop2 = int(input('既然到天堂了，带点土特产回去吧 1.好嘞 2.我不配'))
                if shop2 == 1:
                    # 初始资金
                    money = input('初始金额:\n')
                    money = int(money)
                    # 优惠券
                    coupon = random.randint(1, 30)
                    extract = input('是否需要优惠券 需要y,不需要n\n')

                    print('啊哈哈哈哈哈~~')
                    hh()
                    heihei()

                else:
                    print('凡夫俗子')
                    break
            else:
                print('打回凡间！')
        else:
            print('你是猪啊~笨蛋')
    else:
        print('对不起，我们不去凡间！')
        break
