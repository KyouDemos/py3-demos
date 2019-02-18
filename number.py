# 简单的四则运算
print('123+123: ', 123 + 123)
print('321-123: ', 321 - 123)
print('111-222: ', 111 - 222)
print('4*5: ', 4 * 5)
# 注意输出的值是全精度的"
print('3.2*7:   ', 3.2 * 7)
# 注意输出的值带有小数位"
print('4/2:     ', 4 / 2)
print('5//2:    ', 5 // 2)  # 取整（向下取整）
print('5%2:     ', 5 % 2)  # 取余
print('round(3.1415):', round(3.1415))  # 四舍五入(不保留小数)
print('round(3.1415):', round(3.1415, 1))  # 四舍五入(保留一位小数)
print('round(3.1415):', round(3.1415, 3))  # 四舍五入(保留三位小数)

# 高阶计算
print('2**10:', 2 ** 10)  # 乘方
print('pow(2,10):', pow(2, 10))  # 乘方
print('|-4|', abs(-4))

# 进制转换
print('hex(20):         ', hex(20))  # 10 -> 16
print('oct(20):         ', oct(20))  # 10 -> 8
print('bin(20):         ', bin(20))  # 10 -> 2
print("int('0b10100',2):", int('0b10100', 2))  # 2 -> 10
print("int('10100',2):  ", int('10100', 2))  # 2 -> 10
print("int('0o24',8):   ", int('0o24', 8))  # 8 -> 10
print("int('24',8):     ", int('24', 8))  # 8 -> 10
print("int('0x14',8):   ", int('0x14', 16))  # 16 -> 10
print("int('14',8):     ", int('14', 16))  # 16 -> 10

# math模块
import math

print('π:', math.pi)
print('e:', math.e)  # 自然底数
print('√9:', math.sqrt(9))  # 平方根
print('9 ** (1 / 2):', 9 ** (1 / 2))  # 平方根
print('27 ** (1 / 3):', 27 ** (1 / 3))  # 立方根

# 随机数
import random as rd

print('random.random:', rd.random)
print('random.choice([1,2,3,4]):', rd.choice([1, 2, 3, 4]))

# 小数运算
import decimal

# 对比一下两种计算结果的打印值
print(decimal.Decimal(0.1) + decimal.Decimal(0.1) - decimal.Decimal(0.3))  # -0.09999999999999997779553950745
print(decimal.Decimal('0.1') + decimal.Decimal('0.1') - decimal.Decimal('0.3'))  # -0.1(函数中需要传入字符串)

# 设定全局进度
decimal.getcontext().prec = 2
print(decimal.Decimal(0.1) + decimal.Decimal(0.1) - decimal.Decimal(0.3))  # -0.10
print(decimal.Decimal('0.1') + decimal.Decimal('0.1') - decimal.Decimal('0.3'))  # -0.1

# 分数
from fractions import Fraction

print('Fraction(2, 3):', Fraction(2, 3))  # 函数内必须是数字

# 分数运算
a = Fraction(1, 2)
b = Fraction(1, 3)
print('a + b:', a + b)
print('a - b:', a - b)
print('a * b:', a * b)
print('a / b:', a / b)

# 分数、小数转换
print("Fraction('0.6'):", Fraction('0.6'))  # 3/5(函数中需要传入字符串)
print("Fraction(0.6):", Fraction(0.6))  # 5404319552844595/9007199254740992
print(Fraction(str(1.2 * 4)))

# 集合
x = set('abcdef')
y = set('bdmn')
print('x:', x)
print('y:', y)

x.add('g')
print("x.add('g'):", x)
x.update('h')
print("x.update('h'):", x)
x.pop()
print("x.pop():", x)  # 删除第一个元素
x.remove('h')
print("x.remove('h'):", x)  # 删除指定元素

# 集合运算
print("set('bc') in x:", set('bc') in x)
print('x - y:', x - y)
print('x & y:', x & y)
print('x | y:', x | y)
print('x ^ y:', x ^ y)

# 集合解析
print("{i*2 for i in x}:", {i * 2 for i in x})
