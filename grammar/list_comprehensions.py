import os

# ======================== 列表生成式 List Comprehensions：可以方便的创建 list ===============================

# 生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(1, 11))

# 生成[1x1, 2x2, 3x3, ..., 10x10]：
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# 简化上面写法，使用 List Comprehensions 指定要生成的元素：
L1 = [x * x for x in range(1, 11)]
# for循环后面还可以加上 if 判断，这样我们就可以筛选出仅偶数的平方：
L2 = [x * x for x in range(1, 11) if x % 2 == 0]
# for 循环前面可以加上 if-else，不能只跟 if（条件不满足怎么办）
L3 = [x if x % 2 == 0 else -x for x in range(1, 11)]    # [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

# 还可以使用两层循环，可以生成全排列：
L4 = [m + n for m in 'ABC' for n in 'XYZ']  # L3=['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 把一个list中所有的字符串变成小写：
L = ['HELLO', 'WORLD']
L5 = [s.lower() for s in L]  # L4=['hello', 'world']

# 迭代 dict
d = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
for k, v in d.items():
    print(k, '=', v)

# =============== 运用列表生成式，可以写出非常简洁的代码 =================
# 例1、列出当前目录下的所有文件和目录名：
L6 = [d for d in os.listdir('.')]
