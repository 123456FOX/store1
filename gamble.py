import random

date = int(random.randint(0, 10))
money = 2000
i = 0
count = 1
while True:
    if i <= 10:
        i = i + 1
        count = 10 - i
        num = input("输入数字：\n")
        if num.isdigit():
            num = int(num)

            if num < date:
                money = money - 200
                print("小了", "还剩", count, "次机会")
            elif num > date:
                money = money - 200
                print("大了", "还剩", count, "次机会")
            else:
                money = money + 5000
                print("可以啊！")
                haha = int(input("是否继续？1继续  2退出 \n"))
                if haha == 2:
                    print("走你！")
                    break
                elif haha==1:
                    print("来吧！小宝贝")
                    i = 0
                    date = int(random.randint(0, 10))
                else:
                    print("你在干嘛？！")
                    i = 0
                    date = int(random.randint(0, 10))
    else:
        print("请充钱")