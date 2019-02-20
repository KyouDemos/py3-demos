global s

s = '543'


# 变量s的作用于演示
def func1():
    s = '123'
    print('s1=', s)

    def func1_1():
        global s  # 表名本方法内部的s，是全局变量s
        print('s2=', s)
        s = 'asd'
        print('s3=', s)

    print('s4=', s)  # 此处的s，是func1方法的本地变量s
    return func1_1()  # 在方法func1中返回func1_1方法对象，导致


func1()


# 变量x的闭合的演示
def func2(x):
    def func2_1(y):
        return y ** x

    return func2_1


print([func2(2)(i) for i in range(11)])


# lambda 表达式
def func3(x):
    return lambda n: x ** n


print(func3(2)(3))
