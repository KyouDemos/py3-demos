# “字符串是单个字符的字符串的序列”
s = 'abcd'
print('len(s): ', len(s))
print('s[1]:   ', s[1])      # 正向索引
print('s[-1]:  ', s[-1])     # 反向索引
print('s[1:3]: ', s[1:3])    # 序列分片（左包含）
print('s[:3]:  ', s[:3])     # 序列分片（左边界默认值为0）
print('s[1:]:  ', s[1:])     # 序列分片（右边界默认值为s的长度）

# 字符串重复
print('s*4:    ', s*4)       # 字符串乘法表示字符串重复

# 字符串函数
s = 'abcdbcebc'
print('s:      ', s)
# 返回子字符串的偏移量，没有找到的情况下返回-1
print("s.find('bc',2):", s.find('bc',2))
# 字符串替换（第三个参数可控制替换次数）
print("s.replace('b','B',2):", s.replace('b','B',2))
print('s:      ', s)               # 虽然做了字符替换，但是原字符串不变（字符串不变性）
print("s.split('bc'):", s.split('bc'))
print("s.upper():    ", s.upper())
print(r"(' \n \t' + s + '\t').strip():", (' \n \t' + s + '\t').strip())

# 字符串格式化
print('%s and %s is dfghjk' % ('a', 'b'))
print('{1} and {0} is dfghjk'.format('a', 'b'))

# 其他函数
print("ord('A'):",ord('A'))       # 字母的ASCII编码

# 正则匹配
import re
match = re.match('hello [ ]*(.*)world', "hello python world.")    # 匹配表达式中小括号内的匹配内容会被保存到match内。
print("match.groups():",match.groups())

match = re.match('/(.*)/(.*)/(.*)/(.*)/','/u01/app/crbrq/lib/')
print("match.groups():",match.groups())
match = re.match('/(.*)/','/u01/app/crbrq/lib/')                  # 贪婪式匹配
print("match.groups():",match.groups())