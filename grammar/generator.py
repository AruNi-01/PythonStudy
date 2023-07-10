# 生成器：一边循环一边计算的机制，列表元素可以按照某种算法推算出来，这样可以大大节省内存，用到再推
g = (x * x for x in range(10))
next(g)     # 通过 next 函数获取下一个值，为空时会报错
# 常用：循环遍历
for n in g:
    print(n)


# 如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现

# 输出斐波那契 前 N 个数，默认写法
def fib(N):
    n, a, b = 0, 0, 1
    while n < N:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'


# generator 写法：只需要把 print(b) 改为 yield b 即可
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator函数，调用一个generator函数将返回一个generator
# generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def fib2(N):
    n, a, b = 0, 0, 1
    while n < N:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


g = fib2(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:  # 想要拿到返回值，必须捕获StopIteration错误
        print('Generator return value:', e.value)
        break

