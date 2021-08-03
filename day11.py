class OldPhone:
    __brand = ''

    def __init__(self, brand):
        self.__brand = brand

    def getbrand(self):
        return self.__brand

    def show(self, name):
        print('正在给', name, '打电话')


class NewPhone(OldPhone):
    def call(self):
        print('语音拨号中...')
        super().show('hh')

    def show8(self):
        print('品牌为', super().getbrand(), '的手机很好用...')


old = OldPhone('摩托罗拉')
old.show('zz')
new = NewPhone('诺基亚')
new.call()
new.show8()


class Chief:
    __name = ''
    __age = ''

    def __init__(self, name, age):
        self.__age = age
        self.__name = name

    def getname(self):
        return self.__name

    def getage(self):
        return self.__age

    def rice(self):
        print('厨师', self.__name, '正在蒸饭')


class Chief1(Chief):
    def show(self):
        print('炒菜')


class Chief2(Chief1):
    def zhengfan(self):
        print('蒸饭')

    def chaocai(self):
        print('炒菜')


class test:
    C = Chief2('HHH', 222)
    C.zhengfan()
    C.chaocai()


class Person:
    __age = ''
    __name = ''
    __sex = ''

    def setage(self, age):
        self.__age = age

    def getage(self):
        return self.__age

    def setsex(self, sex):
        self.__sex = sex

    def getsex(self):
        return self.__sex

    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name


class Worker(Person):

    def run(self):
        print('我是工人，我叫', super().getname(), '我', super().getage(), '岁了', '我是', super().getsex())


worker = Worker()
worker.setname('小可爱')
worker.setsex('女孩子')
worker.setage('3')
worker.run()


class Student(Person):
    __XueHao = ''

    def __init__(self, XueHao):
        self.__XueHao = XueHao

    def study(self):
        print(super().getname(), '喜欢学习')

    def sing(self):
        print(super().getname(), '喜欢唱歌')

    def show1(self):
        print('我叫', super().getname(), '我', super().getage(), '岁了', '我是个', super().getsex(),
              '我的学号是', self.__XueHao)


s = Student(1713020129)
s.setname('大明湖畔的夏雨荷')
s.setsex('女孩子')
s.setage('18')
s.show1()
