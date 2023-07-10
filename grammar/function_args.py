# ========================== 1.必填参数 ===============================
def func1(x):
    return x * x


# 调用
func1(2)


# ========================== 2.默认参数 ===============================
def func2(x, y=2):
    return x * y


# 默认参数 坑：L 默认为list []，是一个可变对象，那么多次调用时，就相当于把默认参数改成了前一次调用时对 L 的操作后的值
def func2_1(L=[]):
    L.append('end')
    return L


# 所以：默认参数必须指向不变对象。比如 str、None，这样无论调用多少次都没问题
def func2_2(L=None):
    if L is None:
        L = []
    L.append('end')
    return L


# 调用
func2(1)
func2(1, 2)


# ========================== 3.可变参数 ===============================
# 普通函数
def func3(nums):
    sum = 0
    for n in nums:
        sum = sum + n
    return sum


# 调用，使用 list 或者 tuple
func3([1, 2, 3])
func3((1, 3, 5, 7))


# 上面那样定义只能传入 list 或 tuple，所以我们接下来定义一个可变参数的函数
def func3_1(*nums):
    sum = 0
    for n in nums:
        sum = sum + n
    return sum


# 调用，直接传参
func3_1(1, 2, 3)


# ========================== 4.关键字参数，是一个 dict ===============================
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# 可以只传入必填参数
person('Bob', 19)
# 传入关键字参数，**extra 表示把 extra 这个 dict 的所有 key-value 用关键字参数传入到函数的 **kw 参数，kw 获得的 dict 是 extra 的一份拷贝
extra = {'city': 'WuHan', 'job': 'Engineer'}
person('Bob', 19, **extra)


# ========================== 5.命名关键字参数，用 * 隔开，后面是命名关键字参数 ===============================
def person(name, age, *, city, job):
    print(name, age, city, job)


# 这样就不能只传入必填参数了，命令关键字参数也必须要传入（除非命名关键字参数有默认值）
person('Bob', 19, city='WuHan', job='Engineer')


# ========================== 参数组合 ===============================
# 组合使用时，顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

# 2 必选参数，默认参数，可变参数，关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


# 2 必选参数，默认参数，分隔符，命名关键字参数，关键字参数
def f2(a, b, c=0, *, key, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', key, 'kw =', kw)


# 可以通过 tuple 和 dict 简便地调用
args1 = (1, 2, 3, 4)
kw1 = {'num': 99, 'job': 'Engineer'}
f1(*args1, **kw1)  # a = 1 b = 2 c = 3 args = (4,) kw = {'num': 99, 'job': 'Engineer'}

args2 = (1, 2, 3)
kw2 = {'key': 99, 'job': 'Engineer'}
f2(*args2, **kw2)  # a = 1 b = 2 c = 3 key = 99 kw = {'job': 'Engineer'}
