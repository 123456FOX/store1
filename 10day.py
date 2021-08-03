# 属性: 高度，容积，颜色，材质
class Cup:
    __height = 0
    __volume = 0
    __color = ""
    __material = ""

    def setHeight(self, height):
        self.__height = height

    def setVolume(self, volume):
        self.__volume = volume

    def setColor(self, color):
        self.__color = color

    def setMaterial(self, material):
        self.__material = material

    # 功能:能存放液体
    def save(self, water):
        print('我可以储存', water)

    def myself(self):
        print('我', self.__height, 'cm高',
              '我能装', self.__volume, 'ml的水',
              '我的颜色是', self.__color, '我的材质是', self.__material)


c = Cup()
c.setHeight(20)
c.setColor('绿色')
c.setVolume(20)
c.setMaterial('钢铁')
c.save('敌敌畏')
c.myself()


# 属性 屏幕大小，价格，cpu型号，内存大小，待机时长
# 行为（打字，打游戏，看视频）
class Computer:
    __size = ""
    __price = 0
    __model = ""
    __ram = 0
    __time = 0

    def __init__(self, size, price, model, ram, time):
        self.__size = size
        self.__price = price
        self.__model = model
        self.__ram = ram
        self.__time = time
        print('我', size, '大',
              '我很贵，有多贵呢', price, '块',
              '我的CPU有这么多', ram,
              '我的待机时长是', time)

    def type(self, count):
        print("我今天打了", count, "个字")

    def playGames(self, game):
        print("我今天用电脑玩了", game)

    def watchVideo(self, video):
        print("我用电脑看了", video)


com = Computer(20, 20, 20, 20, 20)
com.type(20)
com.playGames(10)
com.watchVideo(120)
