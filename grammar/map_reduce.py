from functools import reduce


# map() 函数接收两个参数，一个是函数，一个是 Iterable
# map 将传入的函数依次作用到序列的每个元素，并把结果作为新的 Iterator 返回
def func(x):
    return x * x


r = map(func, [1, 2, 3, 4, 5])
# 结果 r 是一个 Iterator，Iterator 是惰性序列，因此通过 list() 函数让它把整个序列都计算出来并返回一个 list
list(r)  # [1, 4, 9, 16, 25]

# 把 list 中的所有元素转为 str
list(map(str, [1, 2, 3, 4, 5]))  # ['1', '2', '3', '4', '5']


# reduce 把一个函数作用在一个序列 [x1, x2, x3, ...] 上，这个函数必须接收两个参数，
# reduce 把结果继续和序列的下一个元素做累积计算，效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add(x, y):
    return x + y


reduce(add, [1, 3, 5, 7, 9])  # 25
# 当然求和运算可以直接用 Python 内建函数 sum()，没必要动用 reduce。


# 如果要把序列 [1, 3, 5, 7, 9] 变换成整数 13579，reduce 就可以派上用场：
def fn(x, y):
    return x * 10 + y


reduce(fn, [1, 3, 5, 7, 9])  # 13579

# 示例：编写一个 str2int
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def f1(x, y):
        return x * 10 + y

    def char2num(c):
        return DIGITS[c]

    # 先用 map，将字符串 s 中的每个字符作用于 char2num（转为数字），再用 reduce 将 list 中的数字变为一个整数
    return reduce(f1, map(char2num, s))

