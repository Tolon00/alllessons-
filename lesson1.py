# коробка для создания данных
# все функции внутри класса называются -- методами
class Kat:
    hvost = True
    usiki = True  # свойства

    # магический метод
    def __init__(self, name, age, color):  # иниту называют конструктором класса
        self.name = name
        self.age = age
        self.color = color

    def m(self):
        self.may()

        # магические методы созданы для того чтобы внедрять стандартнык функции нашим классам, и для каждой функции существует свой магический метод

    def may(self):  # методы
        print(self.name, 'may')

    def __len__(self):  # все магические функции должны лишь возвращать, потому что мы их сразу исползуем
        return len(f'{self.name},{self.color},{self.age}')

    def __str__(self):
        return f'my name is {self.name}\n' \
               f'age is {self.age}\n' \
               f'I am a cat\n' \
               f'{self.hvost}\n' \
               f'#########'


kat2 = Kat('Арген', 4, 'оранжевый')
kat2.name = 'Adyl'
# print(type(kat2))
kat3 = Kat('emir', 2, 'red')

# когда мы создаем свой тип данных к нему не возможно применить стандартные функции
# например print(), len(), abc(), repr()

# kat2.may()
kat2.m()
# print(len(kat2))
# print(kat2.name,kat2.age,kat2.color)
print(kat2)

print(kat3)
