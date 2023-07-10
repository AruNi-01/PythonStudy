# ======================== 切片：py 中 list、tuple、str 都可以进行 slice 操作 ===============================

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

var1 = L[0:3]  # 取 index = 0,1,2
var2 = L[:3]  # 0 可以省略
var3 = L[-2:]  # 取后 2 个
var4 = L[-3:-1]  # 取后面, index = (len-3),(len-2)
var5 = L[:5:2]  # 取前 5 个，每两个取一个
var6 = L[::3]  # 取所有，每三个取一个


# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作
var7 = (0, 1, 2, 3, 4, 5)[:3]


# 字符串'abcde'也可以看成是一种list
var8 = 'ABCDEFG'[:3]

