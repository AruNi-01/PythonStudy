# 关键字 lambda 表示匿名函数，冒号前面的 x 表示函数参数

# lambda x: x * x ===> def f(x): return x * x
list(map(lambda x: x * x, [1, 2, 3, 4, 5]))  # [1, 4, 9, 16, 25]

# 把匿名函数赋值给一个变量
f = lambda x: x * x
f(5)  # 25


# 把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y
