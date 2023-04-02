# get возвращает, set меняет


# множественное наследование
class A:
    def __init__(self, a):
        self.a = a

    def set(self):
        print('это метод класса А')


class B(A):
    pass


class C:
    def set(self):
        print('это метод класса С')

    def __init__(self, c):
        self.c = c


class M(C, B):
    def __init__(self, a, c):
        B.__init__(self, a)
        C.__init__(self, c)

    def __str__(self):
        return f"{self.a} {self.c}"

    def set(self):
        C.set(self)
        super().set()
        A.set(self)
m = M('A', 'C')
print(m)
print(M.mro()) # mro порядок выполнение методов
m.set()
# C.set(m)



class Saving:
    pass

class Checking:
    pass

class Bankacc(Saving, Checking):
    pass

class Bond:
    pass

class Stock:
    pass

class Security(Stock, Bond):
    pass

class Real:
    pass

class Ins(Bankacc, Real):
    pass

class Asset(Bankacc, Security, Real):
    pass

class Interest(Bankacc, Security):
    pass





import math
# print(math.pi)
#
# from math import pi as p
#
# print(p)
#
# from math import *
#
# print(tau,nan)
# встроенные
# from lesson4 import M

# n = M('A', 'C')
# print(n)
# собвственные модули



#внешние модули