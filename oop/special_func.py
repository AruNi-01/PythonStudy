# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。
# Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。
class Student(object):
    def __init__(self, name):
        self.name = name

    # 类似 Java 的 toString() 方法
    def __str__(self):
        return 'Student Object (name: %s)' % self.name

    # 当获取 attr 属性时，如果类中没有，就会到 __getattr__ 中来找。作用：可以针对完全动态的情况作调用。
    def __getattr__(self, attr):
        if attr == 'score':
            return 90
        # 如果 __getattr__ 里也找不到，则会返回 None，所以需要做一下错误处理
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


# 有一个 REST API：http://api.server/user/timeline/list，如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
# 利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    # 利用 __getattr__ 动态拼接 URL
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    # __call__：直接对实例进行方法调用，比如 c = Chain(), c()
    def __call__(self, *args, **kwargs):
        if not len(args):   # 无参数，直接 return，等于没走此方法
            return
        for arg in args:
            if not arg is None:
                return Chain('%s/%s' % (self._path, arg))

    # __repr__：如果直接输入实例，则打印的是地址信息
    __repr__ = __str__


def test_chain():
    # 调用
    path = Chain().status.user.timeline.list
    # 使用实际参数代替，调用 user() 会直接进 __call__ 方法
    path2 = Chain().github('AruNi').repos('1001')

    print(path)  # /status/user/timeline/list
    print(path2)  # /github/AruNi/repos/1001


# ============ iter 和 next：使用 iter 和 next 让 class 具有迭代器的功能 ================
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # fib 数列的初始化值

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个 fib 值
        if self.a > 100:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个 fib 值

    # 像 list 一样通过下表取值
    def __getitem__(self, n):
        if isinstance(n, int):  # n 是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n 是切片
            start = n.start
            stop = n.stop
            if start is None:  # 这样的形式 [:5]
                start = 0
            a, b = 1, 1
            sli = []
            for x in range(stop):
                if x >= start:  # fib 值大于 start 才存入结果集
                    sli.append(a)
                a, b = b, a + b
            return sli


if __name__ == '__main__':
    # 把 Fib 实例作用于 for 循环
    for n in Fib():
        print(n)

    fib = Fib()
    print(fib[3])  # 3
    print(fib[:5])  # [1, 1, 2, 3, 5]

    test_chain()
