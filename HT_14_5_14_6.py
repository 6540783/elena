# Создать три класса: Dog, Cat, Parrot. Атрибуты каждого класса: name, age, master.
# Каждый класс содержит конструктор и методы: run, jump, birthday(увеличивает age на 1), sleep.
# Класс Parrot имеет дополнительный метод fly, Cat - meow, Dog - bark.
# Создать родительский класс Pet, содержащий все общие методы классов
# Dog, Cat, Parrot. Унаследовать Dog, Cat, Parrot от класса Pet. Удалить в
# дочерних классах те методы, которые имеются у родительского класса.
# Создать объект каждого класса и вызвать все его методы.

class Pet:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return f"The pet is running"

    def jump(self):
        return f"The pet is jumping"

    def birthday(self):
        return f"The pet is turning {self.age + 1}"

    def sleep(self):
        return f"The pat is sleepping"


class Dog(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def bark(self):
        return f"The dog is barking"


class Cat(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def meow(self):
        return f"The cat is meowing"


class Parrot(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def fly(self):
        return f"The parrot is flying"

dog = Dog("Archy", 8, "Ann")
cat = Cat("Pussy", 5, "Kate")
parrot = Parrot("Gosha", 3, "Vasilyi")

print(dog.__dict__)
print(dog.run(), dog.jump(), dog.sleep(), dog.birthday(),dog.bark(), sep="\n")
print(cat.__dict__)
print(cat.run(), cat.jump(), cat.sleep(), cat.birthday(),cat.meow(), sep="\n")
print(parrot.__dict__)
print(parrot.run(), parrot.jump(), parrot.sleep(), parrot.birthday(),parrot.fly(), sep="\n")



