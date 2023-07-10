# 高阶函数：参数有包含函数

# 变量可以指向函数
func1 = abs
ten = func1(-10)


# 函数名也是变量
# abs = 10
# abs(-10)    # 报错，此时 abs 已经不是函数了，而是 int


# 高阶函数
def abs_add(num1, num2, func):
    return func(num1) + func(num2)


x, y = -1, -2
func2 = abs
res = abs_add(x, y, func2)  # res = 3
