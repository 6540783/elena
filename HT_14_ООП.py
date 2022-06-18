# Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
# Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
# Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.

# class Dog:
#
#     def __init__(self, height, weight, name, age):
#         self.height = height
#         self.weight = weight
#         self.name = name
#         self.age = age
#
#     def jump(self, sm):
#         return f"Высота прыжка составляет {sm} см"
#
#     def run(self, speed):
#         return f"Скорость бега достигает {speed} км\ч"
#
#     def bark(self, wow):
#         return f"Характерен лай {wow}"
#
# labrador = Dog(45, 60, "Archy", 5)
#
# print(labrador.jump(60), labrador.run(40), labrador.bark("гав-гав"))
# print(labrador.__dict__)

# Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет
# атрибут имени у объекта.
# Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя.

class Dog:

    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self, sm):
        return f"Высота прыжка составляет {sm} см"

    def run(self, speed):
        return f"Скорость бега достигает {speed} км\ч"

    def bark(self, wow):
        return f"Характерен лай {wow}"


    def change_name(self, new_name):
        self.name = new_name

labrador = Dog(45, 60, "Archy", 5)
print(labrador.name)

labrador.change_name("Barchy")

print(labrador.name)

