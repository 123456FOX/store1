import unittest
from calc import Calc


class CalcTest(unittest.TestCase):  # 类就是单元测试的子类
    def test_ruduce(self):
        # 准备数据
        a = 3
        b = 2
        c = 1
        # 调用数据
        calc = Calc()
        sum = calc.ruduce(a, b)
        # 断言
        self.assertEqual(c, sum)

    def test_multi(self):
        # 准备数据
        d = 2
        e = 2
        f = 4
        # 调用数据
        calc1 = Calc()
        sum1 = calc1.multi(d, e)
        # 断言
        self.assertEqual(f, sum1)

    def test_division(self):
        # 准备数据
        g = 1
        h = 1
        i = 1
        # 调用数据
        calc2 = Calc()
        sum2 = calc2.division(g, h)
        # 断言
        self.assertEqual(i, sum2)
