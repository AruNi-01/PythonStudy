# 继承自 object（祖宗类）
class Animal(object):
    name = 'Animal'     # 类属性

    # 构造函数，__ 开头的变量是 private
    def __init__(self, type):
        self.__type = type

    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type

    def run(self):
        print(self.__type, "running...")


class Cat(Animal):
    pass


class Dog(Animal):
    pass


if __name__ == '__main__':
    cat = Cat('cat')
    cat.run()

    dog = Dog('dog')
    dog.run()

    print(Animal.name)      # Animal
    print(isinstance(cat, Animal))  # True

