import time
from threading import Thread
import threading

# 厨师：0.5S造一个面包，3个厨师同时造，当篮子的面包满了等0.5s
# 顾客：3000元，同时去抢面包，当面包不够，顾客需要等1s
# 篮子：最多容纳600个面包，每个2元
money = 3000
num = 0


class Chief(Thread):
    brand = 0
    name = ''
    mutex1 = threading.Lock()

    def run(self) -> None:
        global num
        while True:
            self.mutex1.acquire()
            if num < 600:
                num = num + 1
                self.brand += 1
                time.sleep(0.5)
                print('厨师', self.name, '造了', self.brand, '个面包。')
            else:
                time.sleep(0.5)
            self.mutex1.release()


class Customer(Thread):
    name = ''
    mutex = threading.Lock()

    def run(self) -> None:
        global money, num
        while True:
            self.mutex.acquire()
            if num > 0:
                if money > 2:
                    money = money - 2
                    num = num - 1
                    print('篮子里还剩', num, '个')
                else:
                    break
            else:
                time.sleep(1)
            self.mutex.release()


c = Chief()
c.name = '李大嘴'
b = Chief()
b.name = '小毛'
a = Chief()
a.name = '妈妈'

d = Customer()
e = Customer()
f = Customer()
g = Customer()
h = Customer()
i = Customer()
c.start()
b.start()
a.start()
d.start()
e.start()
f.start()
g.start()
h.start()
i.start()
