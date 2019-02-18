# “字符串是单个字符的字符串的序列”
s = 'abcd'
print('len(s): ', len(s))
print('s[1]:   ', s[1])  # 正向索引
print('s[-1]:  ', s[-1])  # 反向索引
print('s[1:3]: ', s[1:3])  # 序列分片（左包含）
print('s[:3]:  ', s[:3])  # 序列分片（左边界默认值为0）
print('s[1:]:  ', s[1:])  # 序列分片（右边界默认值为s的长度）

# 字符串重复
print('s*4:    ', s * 4)  # 字符串乘法表示字符串重复

# 字符串函数
s = 'abcdbcebc'
print('s:      ', s)
# 返回子字符串的偏移量，没有找到的情况下返回-1
print("s.find('bc',2):", s.find('bc', 2))
# 字符串替换（第三个参数可控制替换次数）
print("s.replace('b','B',2):", s.replace('b', 'B', 2))
print('s:      ', s)  # 虽然做了字符替换，但是原字符串不变（字符串不变性）
print("s.split('bc'):", s.split('bc'))
print("s.upper():    ", s.upper())
print(r"(' \n \t' + s + '\t').strip():", (' \n \t' + s + '\t').strip())

# 字符串格式化
# ## 参考：https://www.cnblogs.com/fat39/p/7159881.html
# ### %形式格式化总结 ###
# %a -- 自动转义字符串（替换元）内的需转义字符
# %d -- 十进制整数
# %c -- 字符,在打印之前将整数转换成对应的Unicode字符。
# %e -- 科学计数法表示（保留小数点后面六位有效数字，e小写）
# %E -- 科学计数法表示（保留小数点后面六位有效数字，E大写）
# %f -- 浮点数（保留小数点后面六位有效数字）
# %F -- 浮点数（保留小数点后面六位有效数字）
# %g -- 通用模式（在保证六位有效数字的前提下，使用小数方式，否则使用科学计数法）
# %G -- 通用模式（在保证六位有效数字的前提下，使用小数方式，否则使用科学计数法）
# %i -- 整数
# %o -- 八进制整数
# %u -- 无符号数
# %x -- 十六进制整数
# %X -- 十六进制整数(字母大写)
# %% -- %

print('root', 'x', '0', '0', sep=':')  # 指定分隔符
print('%s and %s is word' % ('a', 'b'))
print('%(aa)s and %(bb)s is word' % {'aa': 'AA', 'bb': 'BB'})  # 注意匹配内容是花括号包围的

# %.3f- 保留3位小数位
# %.2e- 保留2位小数位，使用科学计数法
# %.4g- 保留4位有效数字，使用小数或科学计数法(自动进行四舍五入)
print("%o,%x,%X,%d,%E,%.2e,%.3f,%.4G" % (63, 63, 63, 63, 63, 10000, 1 / 3, 1234567))

# %10s  —— 右对齐，占位符10位，不够则补位
# %-10s —— 左对齐，占位符10位，不够则补位
# %.2s  —— 截取2位字符串
# %10.2s—— 10位占位符，截取两位字符串
print('%s' % 'hello world')  # 字符串输出
print('%20s' % 'hello world')  # 右对齐，取20位，不够则补位
print('%-20s' % 'hello world')  # 左对齐，取20位，不够则补位
print('%.2s' % 'hello world')  # 取2位
print('%10.2s' % 'hello world')  # 右对齐，取2位
print('%-10.2s' % 'hello world')  # 左对齐，取2位

# ### format形式的格式化 ###
# 'b' -- 二进制。将数字以2为基数进行输出。
# 'c' -- 字符。在打印之前将整数转换成对应的Unicode字符。
# 'd' -- 十进制整数。将数字以10为基数进行输出。
# 'o' -- 八进制。将数字以8为基数进行输出。
# 'x' -- 十六进制。将数字以16为基数进行输出，9以上的位数用小写字母。
# 'e' -- 幂符号。用科学计数法打印数字。用'e'表示幂。
# 'g' -- 一般格式。将数值以fixed-point格式输出。当数值特别大的时候，用幂形式打印。
# 'n' -- 数字。当值为整数时和'd'相同，值为浮点数时和'g'相同。不同的是它会根据区域设置插入数字分隔符。
# '%' -- 百分数。将数值乘以100然后以fixed-point('f')格式打印，值后面会有一个百分号。
print('{0:b}'.format(3))  # 二进制
print('{:d}'.format(42))  # 十进制
print('{:o}'.format(42))  # 八进制
print('{:x}'.format(42))  # 十六进制
print('{:X}'.format(42))  # 十六进制
print('{:c}'.format(65))  # 按照ASCII编码表将数字转成字母
print('{:e}'.format(20))  # 科学计数法
print('{:.2e}'.format(20))  # 指定位数的科学计数法
print('{:g}'.format(20.123456))  # 默认六位有效数字（自动四舍五入）
print('{:.4g}'.format(201254.123))  # 指定4位有效数字（自动四舍五入）

print('{1} and {0} is word'.format('a', 'b'))
print('{aa} and {bb} is word'.format(aa='AA', bb='BB'))
print('{aa} and {bb} is word'.format(**{'aa': 'AA', 'bb': 'BB'}))  # **表示以字典的方式传值
print("i am {0[0]}, age {0[1]}, really {0[2]}".format([1, 2, 3], [11, 22, 33]))  # 读取数组的元素
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))  # 在前面加“#”，则带进制前缀

# 其他函数
print("ord('A'):", ord('A'))  # 字母的ASCII编码

# 正则匹配
import re

match = re.match('hello [ ]*(.*)world', "hello python world.")  # 匹配表达式中小括号内的匹配内容会被保存到match内。
print("match.groups():", match.groups())

match = re.match('/(.*)/(.*)/(.*)/(.*)/', '/u01/app/crbrq/lib/')
print("match.groups():", match.groups())
match = re.match('/(.*)/', '/u01/app/crbrq/lib/')  # 贪婪式匹配
print("match.groups():", match.groups())
