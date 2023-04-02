 # три парадигмы ООП
class Human:  # суперкласс/родительский класс
    # a = 1 свойства
    # конструктор
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def age1(self):
        self.age *= 2
        print(self.age)

    def __str__(self):
        return f'{self.name},{self.age}'


# наследование

# class Student(Human): ... #заглушка # дочерний класс
class Student(Human):
    def age2(self):
        self.age /= 2
        print(self.age)
    def h(self):
        super().age1()

human = Human('Абил', 14)


# human.age1()


# print(student)
# student.age1()
# student.age1()
# student.age2()
# print(student)


# Student.age2(human)


class Tea(Student):
    def __init__(self, name, age, money):
        super().__init__(name,age)
        Human.__init__(self,name,age)
        self.money = money


    def age2(self):
        self.age **= 2
        print(self.age, 'это метод класса Tea')

    def age1(self):
        self.age += 2
        print(self.age)

    def supermetod(self):
        self.age1() # ушул класстан издейт биринчи
        super().age1() # супер будет искать у наследованных классах
        super().h()
        self.age2()
        super().age2()
        print('#######')

    # полиморфизм - это изменение поведение у наследованных методов


student = Student('Жаннат', 19)
tea = Tea('Даниель', 9,'1сом')
# tea.age2()
# tea.age1()
tea.supermetod()
print(tea.age)
tea.supermetod()

print(tea.age)
# student.age2()
# tea.age2()
#
print(Tea.mro())
# print(Human.mro())

f=Tea('бека',5,88888)
f.supermetod()
print(f.age)