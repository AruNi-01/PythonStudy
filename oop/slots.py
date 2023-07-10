# 创建了一个 class 的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
# 动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
class Animal(object):
    # 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性。
    # __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的，除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
    __slots__ = ('color', 'age', 'set_color')


def set_color(self, color):
    self.color = color


if __name__ == '__main__':
    animal = Animal()

    # 给实例绑一个属性
    animal.age = 13
    print(animal.age)  # 13

    # 给实例绑一个方法
    from types import MethodType

    animal.set_color = MethodType(set_color, animal)  # 给实例绑定一个方法
    animal.set_color('black')  # 调用实例方法
    print(animal.color)  # black

    # 给一个实例绑定的方法，对另一个实例是不起作用的，所以可以给class绑定方法
    Animal.set_color = set_color
    # 给class绑定方法后，所有实例均可调用：
    a1 = Animal()
    a1.set_color('pink')
    print(a1.color)     # pink
    a2 = Animal()
    a2.set_color('white')
    print(a2.color)     # white

