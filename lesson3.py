# инкапсуляция     1. структирирование 2. скрытие или защищенность каких либо методов или аргументов
# три уровня защищенности
# 1. открытый
# 2. _=закрытый
# 3. __=скрытый


# get возвращает, set меняет
# геттери и сеттери это просто методы которые позволяют достать и поменять его

# _=protected
# __ скрытие методов
class Bank:
    def __init__(self, name, money, key):
        self.name = name
        self.__money = money
        self._key = key

    def __str__(self):
        return f'{self.name}: {self.__money}'

    # def keys(self):
    # print(self._key)

    def keys(self):
        self._printKey()

    def _printKey(self):
        print(self._key)

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money


user = Bank('жаннат', 4_000_000, '12edswadw')
user.set_money(3000)
print(user.get_money())
# user.keys()
# user.key = '1234'
# user.keys()
# # print(user.key)
# user._key = 1234
# print(user.key, user._key)

# user.__money = 10000000000000000
# print(user.__money)

# user._Bank__money = 1000000000
print(user)
# print(user.__money)


# print(user.__dir__())