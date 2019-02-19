import pickle

# 文件
s = 'qwerty'

# ### 写入文件 ###
# 一般写入文件
f = open('demo.txt', 'w')
f.writelines(list(s))
f.write('\n')
f.write(s)
f.close()

# 避免\n的写入文件方式
f = open('demo_print.txt', 'w')
print('12345', file=f)
print('qwerty', file=f)
f.close()

# 将对象写入文件
f = open('demo1.txt', 'wb')
l = list(s)
pickle.dump(l, f)
f.close()

# ### 读取文件 ###
# 一般读取文件
f = open('demo.txt')  # 默认为读取文件
for l in f:
    print(l.strip())
f.close()

# 从文件读取对象
f = open('demo1.txt', 'rb')
print(pickle.load(f))
f.close()
