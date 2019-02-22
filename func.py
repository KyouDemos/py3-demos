global s

s = '543'


# 变量s的作用于演示
def func1():
    s1 = '123'
    print('s1=', s1)

    def func1_1():
        global s  # 声明本方法内部的s，是全局变量s
        s = s + '2'
        print('s2=', s)

        nonlocal s1  # s1变量是func1方法中的声明的变量
        s1 = s1 + '4'
        print('s3=', s1)

    print('s4=', s1)  # 此处的s1，是func1方法的本地变量s1
    print('s5=', s)  # 此处的s，是全局变量s
    return func1_1()  # 在方法func1中返回func1_1方法对象，导致


func1()
print('s6=', s)


# 变量x的闭合的演示
def func2(x):
    def func2_1(y):
        return y ** x

    return func2_1


print(func2(2)(3))  # 3 ** 2 = 9


# lambda 表达式
def func3(x):
    return lambda n: x ** n


print(func3(2)(3))  # 2 ** 3 = 8

# 参数

x = 'x'
y = [1, 2]


def f4(a, b):
    a = 'a'
    b[0] = 'b'


f4(x, y)

print('x', x, sep=':')  # x的值没变，因为在f4函数中对本地变量a做了赋值，不影响全局变量x的值。
'''
y序列的第一个元素被改变了，因为在调用f4函数时，本地变量b和全局变量y同时指向了序列[1,2]的内存地址。
当通过本地变量b改变序列[1,2]的元素时，由于b,y指向相同的序列，因此y的值也自然被改变了。
'''
print('y', y, sep=':')

# 避免可变参数修改问题
z = [1, 2]
f4(x, z[:])
print('x', x, sep=':')
print('z', z, sep=':')

# 递归函数
l = [1, [2, [3, 4], 5], [6, 7]]


def f5(l):
    s = 0
    print('=' * 10)
    print('l:', l)
    for x in l:
        print('x:', x)
        if not isinstance(x, (list, tuple)):
            s += x
            print('s:', s)
        else:
            s += f5(x)
            print('s:', s)
    return s


print(f5(l))
