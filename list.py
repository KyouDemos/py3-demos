# 序列声明
lst = [123, '123', 1.23]  # 同一个序列内可以同时包含多种不同数据类型的元素。
print('lst:', lst)

# 序列不可变操作
print('len(lst): ', len(lst))
print('lst[1]:   ', lst[1])  # 正向索引
print('lst[-1]:  ', lst[-1])  # 反向索引
print('lst[1:3]: ', lst[1:3])  # 序列分片（左包含）
print('lst[:3]:  ', lst[:3])  # 序列分片（左边界默认值为0）
print('lst[1:]:  ', lst[1:])  # 序列分片（右边界默认值为s的长度）

lst0 = ['bb', 'aa', 'cc']
print('lst + lst0:', lst + lst0)  # 序列拼接
print('lst:', lst)  # 两个序列的加法拼接出一个新的序列，但是原来的两个序列不发生变化

# 序列可变操作
lst.append(321)  # 在序列末尾追加元素
print('lst.append(321):', lst)
lst.insert(1, 222)  # 在制定坐标插入元素
print('lst.insert(1,222):', lst)
lst.pop()  # 默认删除末尾元素
print('lst.pop():', lst)
lst.pop(1)  # 删除指定坐标的元素
print('lst.pop(1):', lst)
l = ['abc', 'ABD', 'aBe']
l.sort()  # 序列排序
print('l.sort():', l)
l.sort(key=str.lower)  # 将字母转小写后排序
print('l.sort(key=str.lower):', l)
l.reverse()  # 倒叙排列
print('l.reverse():', l)

# 多维序列
lst.append(lst0)
print('lst.append(lst0):', lst)
print('len(lst):', len(lst))
print('lst[-1]:', lst[-1])
print('lst[-1][1]:', lst[-1][1])  # 多维序列的数据定位方式
