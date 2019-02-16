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
print('root', 'x', '0', '0', sep=':')  # 指定分隔符
print('%s and %s is word' % ('a', 'b'))
print('{1} and {0} is word'.format('a', 'b'))
print('%(aa)s and %(bb)s is word' % {'aa': 'AA', 'bb': 'BB'})  # 注意匹配内容是花括号包围的
print('{aa} and {bb} is word'.format(aa='AA', bb='BB'))
print('{aa} and {bb} is word'.format(**{'aa': 'AA', 'bb': 'BB'}))  # **表示以字典的方式传值
print("i am {0[0]}, age {0[1]}, really {0[2]}".format([1, 2, 3], [11, 22, 33]))  # 读取数组的元素

# %o —— oct 八进制
# %d —— dec 十进制
# %x —— hex 十六进制
# %X —— hex 十六进制
# %f —— 保留小数点后面六位有效数字
# %F —— 保留小数点后面六位有效数字
# %.3f- 保留3位小数位
# %e —— 保留小数点后面六位有效数字，指数形式输出
# %E —— 保留小数点后面六位有效数字，指数形式输出
# %.3e- 保留3位小数位，使用科学计数法
# %g —— 在保证六位有效数字的前提下，使用小数方式，否则使用科学计数法
# %G —— 在保证六位有效数字的前提下，使用小数方式，否则使用科学计数法
# %.3g- 保留3位有效数字，使用小数或科学计数法
print("%o,%x,%X,%d,%E,%.2e,%.3f" % (63, 63, 63, 63, 63, 10000, 1 / 3))

# %s    —— 字符串
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

# ##总结##
# %a    -- 自动转义字符串（替换元）内的需转义字符
# %d    -- 十进制整数
# %c    -- 字符
# %e    -- 科学计数法表示（保留小数点后面六位有效数字，e小写）
# %E    -- 科学计数法表示（保留小数点后面六位有效数字，E大写）
# %f    -- 浮点数（保留小数点后面六位有效数字）
# %g    -- 通用模式（在保证六位有效数字的前提下，使用小数方式，否则使用科学计数法）
# %G    -- 通用模式（在保证六位有效数字的前提下，使用小数方式，否则使用科学计数法）
# %i    -- 整数
# %o    -- 八进制整数
# %u    -- 无符号数
# %x    -- 十六进制整数
# %X    -- 十六进制整数(字母大写)
# %%    -- %

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
