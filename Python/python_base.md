---
title: 千行代码入门Python
---

开篇：

这篇大部分的内容是直接转自知乎《千行代码入门Python》中间也加了很多，再写这篇的时候，发现我自己也遗忘了很多知识点， 所以一边巩固知识点， 一边填完了这个坑

[TOC]

# 1. Python数据类型: 哈希类型、不可哈希类型

```Python
# 哈希类型
'数字类型: int, float, decimal.Decimal, fractions.Fraction, complex'
'字符串类型: str, bytes'
'元组: tuple'
'冻结集合:frozenset'
'布尔类型: True, False'
'None'
# 不可哈希类型: 原地可变类型：list、dict和set。他们不可以作为字典的key

# 哈希类型----------------------------------------------
# =======================================================================
a = 1211
type(a)  # int类型 1, 0, 999
b = 12.3
type(b)  # float类型， 1.， 0.， 1.2e-10
c = 'hello, world'
type(c)  # str类型， 字符串等
d = bytes(2)
type(d)  # bytes类型 b'\x00\x00', 其中bytes()函数可以直接进行强制类型转化
tuple1 = (2, 3, 4)
type(tuple1)  # tuple类型, 称作元组
bool1 = False
type(bool1)  # 布尔类型， bool类型, True or False
x = None
type(x)  # NoneType 空类型

# ========================数字相关模块======================================================

import decimal
from decimal import Decimal
dec = Decimal('0.01') + Decimal('0.02')  # decimal.Decimal类型 返回Decimal('0.03')  数字相关模块
type(dec)

from fractions import Fraction
x = Fraction(4, 6)  # 分数类型 4/6
x = Fraction('0.25')  # fractions.Fraction类型 分数类型1/4 接收字符串类型的参数
type(x), type(dec)

# 不可哈希类型-----------------------------------------------------
list1 = [1, 2, 3, 4, 4]  # 可使用type()函数查看其类型， 后面将不再写出，list类型(列表)
set1 = set(list1)  # 集合set， 使用set()函数可以将list， tuple类型的数据强制转化成set，
#并且可以达到去重的作用
dict1 = {1: 'hello', 2: 'world'}
for key, value in dict1.items():
    print('%s:%s' %(key, value))  # 字典类型， 同样可以使用dict()函数进行强制转换
# 可以使用for循环将并调用dict的items方法将key和value分别打印出来
```

# 2. 数字常量

```python
1234, -1234, 0, 999999999                    # 整数
1.23, 1., 3.14e-10, 4E210, 4.0e+210          # 浮点数
0o177, 0x9ff, 0X9FF, 0b101010                # 八进制、十六进制、二进制数字
3+4j, 3.0+4.0j, 3J                           # 复数常量，也可以用complex(real, image)来创建
hex(I), oct(I), bin(I)                       # 将十进制数转化为十六进制、八进制、二进制表示的“字符串”
int(string, base)                            # 将字符串转化为整数，base为进制数
# 2.x中，有两种整数类型：一般整数（32位）和长整数（无穷精度）。可以用l或L结尾，迫使一般整数成为长整数
float('inf'), float('-inf'), float('nan')    # 无穷大, 无穷小, 非数
```
# 3. 数字的表达式操作符

```python
yield x                                      # 生成器函数发送协议
lambda args: expression                      # 生成匿名函数
x if y else z                                # 三元选择表达式
x and y, x or y, not x                       # 逻辑与、逻辑或、逻辑非
x in y, x not in y                           # 成员对象测试
x is y, x is not y                           # 对象实体测试
x<y, x<=y, x>y, x>=y, x==y, x!=y             # 大小比较，集合子集或超集值相等性操作符
1 < a < 3                                    # Python中允许连续比较
x|y, x&y, x^y                                # 位或、位与、位异或
x<<y, x>>y                                   # 位操作：x左移、右移y位
+, -, *, /, //, %, **                        # 真除法、floor除法：返回不大于真除法结果的整数值、取余、幂运算
-x, +x, ~x                                   # 一元减法、识别、按位求补（取反）
x[i], x[i:j:k]                               # 索引、分片、调用
int(3.14), float(3)                          # 强制类型转换
```
# 4. 整数可以利用bit_length函数测试所占的位数 

```python
a = 1;       a.bit_length()    # 1
a = 1024;    a.bit_length()    # 11
```
# 5. Python中的魔法方法repr和str 显示格式的区别

```python
__repr__() # 默认的交互模式回显， 产生的结果看起来他们就像是代码
__str__() # 修改打印语句的格式，转化成一种对用户更加友好的格式

# 例
class Vector(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __repr__(self):
		return 'Vector(%r, %r)' % (self.x, self.y)
    
    def __str__(self):
        return '%s, %s' % (self.x, self.y)
    
v1 = Vector(2, 3)
# __repr__和__str__如果当只想实现这两个特殊方法的其中一个， 选择__repr__是更好的选择(来自流畅的Python)
```
# 6. 集合set

```python
# 集合set
"""
    set是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素。
    set支持union(联合), intersection(交), difference(差)和symmetric difference(对称差集)等数学运算。
    set支持x in set, len(set), for x in set。
    set不记录元素位置或者插入点, 因此不支持indexing, slicing, 或其它类序列的操作
    """
s = set([3, 4, 2, 12, 221, 1421])  # 创建一个集合返回{2, 3, 4, 12, 221, 1421}
t = set('hello')  # 创建一个唯一字符串的集合返回值{'e', 'h', 'l', 'o'}， 可见集合是无序的
a = t.union(s)  # t和s的并集， 也可写成 t | s
b = t.intersection(s)  # t和s 的交集， 也可写成 t & s
c = t.difference(s)  # 差集 也可写成 t - s
d = t.symmetric_difference(s)  # 对称差集 也可以写成 
t.add('x')  # 添加一个item
t.remove('h')  # 删除一个item
s.update([10, 21, 42])  # 利用[...]更新s集合
s.issubset(t)  # 测试是否s中的每一个元素都在t中， 或写成 s <= t
s.issuperset(t)  # 测试是否t中的每一个元素都在s中, 或写成 s >= t
d = s.copy()  # 复制
s.discard(2)  # 删除s中的2
s.clear()  # 清空s
set1 = {x for x in [1, 2, 3, 4]}  # 集合生成式， 集合解析， 结果{1, 2, 3, 4}
set1.pop()  # 由于set是无序的，所有pop并不一定是删除最后一个值
```
# 7. 集合frozenset， 不可变对象

```python
"""
set是可变对象，即不存在hash值，不能作为字典的键值。同样的还有list等(tuple是可以作为字典key的)
frozenset是不可变对象，即存在hash值，可作为字典的键值
frozenset对象没有add、remove等方法，但有union/intersection/difference等方法
"""
a = set([1, 2, 3])
b = frozenset()
b.add(a)                     # error: set是不可哈希类型
b.add(frozenset(a))          # ok，将set变为frozenset，可哈希
```
# 8. 布尔类型

```python
# 布尔类型
a = True  # bool类型， 真
list1 = []
if list1:
    print(True)
else:
    print(False)   # 当列表，字符串， 集合等长度为0的时候， 同样会返回False
isinstance(False, int)  # bool类型属于整数， 所以返回True
True == 1  # 返回True， 应为1对应的bool值为True所以两者相等
True is 1  # 返回False， 因为True为bool类型， int类型类型不同，所以返回False
```
# 9. 列表

````python
# 列表
list1 = [1, 2, 3, 4]   # 常见的创建列表的方式
list2 = [i for i in range(10)]  # 列表推导式  返回[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ================================================================================
list2[0]  # 索引查找， 返回第一个数据， 0
list2.pop()  # 去除掉最后一个 删除9
list2.pop(0)  # 通过索引指定想删除的数据 删除0
list1.remove(1)  # 选定列表中想要删除的值进行删除, 返回[2, 3, 4]
list1.index(2)  # 查找指定元素的索引
list1.append(5)  # 在列表的最后面添加一个item
list1.append(4)
list1.append(7)
list1.append(2)   # list1此时为[2, 3, 4, 5, 4, 7, 2]
list1.sort(reverse=True)  # 对list1进行排序, 会直接改变列表的值, reverse属性默认为False， 升序排列， True为降序排列
sorted(list1)  # 同样可以对列表进行排序， 但不会改变当前列表的值， 返回[2, 2, 3, 4, 4, 5, 7]
list1.count(2)  # 查找列表中某个元素中的个数
list1.copy()  # 对列表进行浅复制
list1.clear()  # 清空list
# 最后注：列表中基础方法还有很多， 在这里我只把最长用的一些列举出来了
# ===================================列表高级用法=====================================================
list1 = [2, 1, 23, 4, 12, 5, 3, 23]
list2 = list1
id(list2), id(list1)  # python中规定的，当两个变量在赋值的时候，他们等于的值相同，且类型也相同， 那么为一个对象的同一个引用
list1[0:]  # 切片操作， 返回[2, 1, 23, 4, 12, 5, 3, 23]
list3 = list1[0:]
id(list1), id(list3)  # 使用切片的方式，复制该列表的值给另一个列表， 将不会出现上面对同一个对象引用的情况
list1[::-1]  # 使用切片， 可以让列表很容易实现列表顺序的翻转,  list1[start:stop:step]  切片操作的三个参数分别为起始索引， 结束位数， 分割数
list1[1:3] = [1, 2, 3]  # 同样也可以使用切片的方式更新列表中部分数据 返回[2, 1, 2, 3, 4, 12, 5, 3, 23]
list1[1:3] = []  # 当然包括了移除数据 list1值变为[2, 3, 4, 12, 5, 3, 23]， 对比上一条数据， 很明显， 前面三个数据被移除了
list2   # 这个时候打印一下最开始通过list1直接赋值的list2会发现虽然在上面我们并没有对list2进行操作， 但是list2的值也随着list1的值进行改变了
# list2返回[2, 3, 4, 12, 5, 3, 23]
list3  # 同样打印通过对list切片赋值的list3， list3的值并没用发生变化 返回[2, 1, 23, 4, 12, 5, 3, 23]
list1 + list3  # 通过这个方法可以将两个列表进行合并 返回[2, 3, 4, 12, 5, 3, 23, 2, 1, 23, 4, 12, 5, 3, 23]
# list1 - list3  # 但是使用- 会报错

# ==================================列表操作的补充==================================================================
# 上述的操作， 可以算是列表中常见的操作方法了， 下面将会简绍一些特别有用的操作方法

# 第一个方法是对，*args可变参数的使用
*list4, a, _ = list3
list4, a  # 使用*这种方式，可以将列表拆分为几个部分， 返回 [2, 1, 23, 4, 12, 5], 3,   即a为倒数第二个数， 
# list4为去掉倒数第二个和最后一个数后剩下的所有值
# 上面的这种方法使用与所有可迭代的数据类型， 如tuple, dict, list, set等
str1 = 'hello, world'  
list(str1)  # 使用list函数可以对字符串， 集合，等进行强制转化成列表
# 当需要对一个列表中的数做去重处理的时候， 我们可以通过set()方法将该列表强制转化为集合， 由于集合不可重复的特性，完成去重操作
dict1 = dict(zip(list1, list2))
dict1   # 可以通过zip函数将两个等长的列表合并，并使用dict函数强制转化成字典形式, 返回{2: 2, 3: 3, 4: 4, 12: 12, 5: 5, 23: 23}
# 当然列表中肯定还存在多维列表， 且多维列表同样也可以进行多维切片操作。
````
# 10. 字符串

```python
str1 = 'hello, world'  # 字符串的创建方法
str2 = '''
    asldsldlasldlas. sldlasldsdxm,ck
    asljdksadksakldk
'''                    # 可以使用这种方法来进行对行字符串的赋值
str1[::-1]   # 同样的字符串也可以像列表一样进行切片操作， 在这里就不多说了， 有兴趣的可以自己去尝试
str1.upper()  # 全部改为大写的方法
str1.lower()  # 全部改为小写的方法
str1.strip()  # 删除两端空格的方法
str1.count('l') # 计算该字符串中，指定元素的个数
str1.isdigit()  # 判断字符串中是否只有数字组成
str1.isalpha()  # 判断字符串中是否只有字母组成
str1.find('h')  # 从左开始查找， 找到第一个自定元素，便返回他的索引
str1.rfind('l')  # 从右开始查找， 找到第一个指定元素， 便返回他的索引
str1.replace(',', ':')  # 将字符串中指定的元素替换成另一个， 两个参数分别是， 字符串中的某个元素或者元素组合，  想要替换成的值
sorted(str1)  # sorted的方法可以对字符串的值进行排序，但是这样会返回一个列表类型
str1.split(',')  # 将字符串已指定的字符进行分割， 返回一个列表, 返回['hello', ' world']
# 由于字符串在使用list()函数进行强制类型转化的时候， 会将字符串中的所有元素都变成列表中的一个元素，
# 所以大部分时间，想要对一个字符串进行列表形式的操作, 我们都可以使用split()将字符串分割成列表再进行操作

S = ''                                  # 空字符串
S = "spam’s"                            # 双引号和单引号相同
S = "s\np\ta\x00m"                      # 转义字符
S = """spam"""                          # 三重引号字符串，一般用于函数说明
S = r'\temp'                            # Raw字符串，不会进行转义，抑制转义
S = b'Spam'                             # Python3中的字节字符串
S = u'spam'                             # Python2.6中的Unicode字符串
s1+s2, s1*3, s[i], s[i:j], len(s)       # 字符串操作
'a %s parrot' % 'kind'                  # 字符串格式化表达式
'a {1} {0} parrot'.format('kind', 'red')# 字符串格式化方法
for x in s: print(x)                    # 字符串迭代，成员关系
[x*2 for x in s]                        # 字符串列表解析
','.join(['a', 'b', 'c'])               # 字符串输出，结果：a,b,c

# 字符串转换工具：
int('42'), str(42)                      # 返回(42, '42')
float('4.13'), str(4.13)                # 返回(4.13, '4.13')
ord('s'), chr(115)                      # 返回(115, 's')
int('1001', 2)                          # 将字符串作为二进制数字，转化为数字，返回9
bin(13), oct(13), hex(13)               # 将整数转化为二进制/八进制/十六进制字符串，返回('0b1101', '015', '0xd')

#-- 另类字符串连接
name = "wang" "hong"                    # 单行，name = "wanghong"
name = "wang" \
"hong"                          # 多行，name = "wanghong"
```
# 11. 字符串补充

```python
#-- Python中的字符串格式化实现1--字符串格式化表达式
"""
基于C语言的'print'模型，并且在大多数的现有的语言中使用。
通用结构：%[(name)][flag][width].[precision]typecode
"""
"this is %d %s bird" % (1, 'dead')                          # 一般的格式化表达式
"%s---%s---%s" % (42, 3.14, [1, 2, 3])                      # 字符串输出：'42---3.14---[1, 2, 3]'
"%d...%6d...%-6d...%06d" % (1234, 1234, 1234, 1234)         # 对齐方式及填充："1234...  1234...1234  ...001234"
x = 1.23456789
"%e | %f | %g" % (x, x, x)                                  # 对齐方式："1.234568e+00 | 1.234568 | 1.23457"
"%6.2f*%-6.2f*%06.2f*%+6.2f" % (x, x, x, x)                 # 对齐方式：'  1.23*1.23  *001.23* +1.23'
"%(name1)d---%(name2)s" % {"name1":23, "name2":"value2"}    # 基于字典的格式化表达式
"%(name)s is %(age)d" % vars()                              # vars()函数调用返回一个字典，包含了所有本函数调用时存在的变量

#-- Python中的字符串格式化实现2--字符串格式化调用方法
# 普通调用
"{0}, {1} and {2}".format('spam', 'ham', 'eggs')            # 基于位置的调用
"{motto} and {pork}".format(motto = 'spam', pork = 'ham')   # 基于Key的调用
"{motto} and {0}".format('ham', motto = 'spam')             # 混合调用
# 添加键 属性 偏移量 (import sys)
"my {1[spam]} runs {0.platform}".format(sys, {'spam':'laptop'})                 # 基于位置的键和属性
"{config[spam]} {sys.platform}".format(sys = sys, config = {'spam':'laptop'})   # 基于Key的键和属性
"first = {0[0]}, second = {0[1]}".format(['A', 'B', 'C'])                       # 基于位置的偏移量
# 具体格式化
"{0:e}, {1:.3e}, {2:g}".format(3.14159, 3.14159, 3.14159)   # 输出'3.141590e+00, 3.142e+00, 3.14159'
"{fieldname:format_spec}".format(......)
# 说明:
"""
fieldname是指定参数的一个数字或关键字, 后边可跟可选的".name"或"[index]"成分引用
format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
fill        ::=  <any character>              #填充字符
align       ::=  "<" | ">" | "=" | "^"        #对齐方式
sign        ::=  "+" | "-" | " "              #符号说明
width       ::=  integer                      #字符串宽度
precision   ::=  integer                      #浮点数精度
type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
"""
# 例子:
'={0:10} = {1:10}'.format('spam', 123.456)    # 输出'=spam       =    123.456'
'={0:>10}='.format('test')                    # 输出'=      test='
'={0:<10}='.format('test')                    # 输出'=test      ='
'={0:^10}='.format('test')                    # 输出'=   test   ='
'{0:X}, {1:o}, {2:b}'.format(255, 255, 255)   # 输出'FF, 377, 11111111'
'My name is {0:{1}}.'.format('Fred', 8)       # 输出'My name is Fred    .'  动态指定参数
```



# 12. 元组

```python
# Python的元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
tuple1 = (1, 2, 3)  # 元组的创建
x, y, z = tuple1
x, y, z  # 通过元组可以很容易个变量赋值
print('%s, %s, %s' % tuple1)  # 在打印的时候也可以使用这种方法进行打印
# 像上面简绍的列表， 字符串， 集合等， 元组也是可迭代的， 可以使用for循环， 循环打印他所有item
tuple1[0:]  # 元组同样具有切片操作， 切片操作其实就是调用了slice()函数, 但是tuple不可直接访问slice函数
tuple1.index(2)  # 查找元组中某个指定值得下标
tuple1.count(2)  # 计算指定元素在该元组中的个数
# 由于tuple是不可变的，所有在tuple中，少了添加，删除等方法，如果想要对元组的数据进行添加修改删除等操作， 可以将元组
# 通过list()函数转化为列表类型再进行操作
tuple2 = (i for i in range(10))
next(tuple2)  # 返回0， 第一个数据， 元组生成式， 这样生成的元组和列表推导式生成的列表，不同， 元组生成式生成的是一个generator生成器, 
# 需要使用next()方法才能获取其元素的值， 但当使用for循环的时候， 由于其会自动调用python内置的__next__()方法， 可以等效于使用了next()
```
# 13. 字典

```python
#-- 常用字典常量和操作
d = {1: 'list', 2: 'tuple'}  # 创建字典
d = dict.fromkeys(['list', 'tuple'], 'str')
d = dict(name='Sherlock', age = '40')
d = dict(zip(['name', 'age'], ['Sherlock', '40']))  # 上面几种方式都是创建dict字典的方式
d.keys()  # 获取当前字典所有的key
d.values()  # 获取当前字典所有的values
d.items()  # 获取同时获取当前字典的所有的key和value， 通过这个方法进行循环遍历可以分别打印出，
# 相同隐式索引对应的key和value
d.get('name')  # 通过这种获取key的方法查找指定索引对应的value,
# 也可以写成d['name']（这种方法在当前字典中没有指定的key的时候， 会报错， 
# 所以在不确定字典中是否存在想要查找的key的时候， 应该使用这种方法）
d.update({'name': 'Qingle', 'age': '22'})  # 合并字典， 如果存在相同的键值对， 新的字典会覆盖旧的字典
d.pop('name')  # 删除一个自定的键值对 pop(key, d[key])
d.update({'name': 'Qingle', 'age': '22'}) 
d.popitem()  # 删除字典中的一项
d.setdefault('name', 'Qingle')  # 设置字典中的某一项的默认值, setdefault(k, d)
# 如果有k存在， 就返回d[k], 否则返回d
del d  # 完全删除字典
d = dict(zip(['name', 'age'], ['Sherlock', '40']))
del d['name']  # 删除字典中的某一项
'name' in d  # 判断key是否在字典中  'name' not in d 是否不再d中
d[(1, 2, 3)] = 2  # 元组也可以作为字典的keyss
dict1 = {'中国': 66129843, '日本': 13113, '美国': 1313331}
sorted(dict1.items(), key=lambda x: x[1], reverse=True)  # 字典通过value排序的方法
```
# 14. 循环与条件语句

```python
# 这个部分主要用三个例子来描述
# 1.猜拳： 主要介绍条件语句， if elif else
import random

index = random.randint(0, 2)  # randint为左闭右闭区间， index可以随机取得0， 1， 2, 在这里我们将它当做电脑的出拳
people_num = int(input('请出拳：1，剪刀  2，石头  3，布'))  # people_num为python pep8规定的命名规则
# 还可以使用驼峰命名法， 在这里可以写成peopleNum, java, c, c++ 语言等多使用驼峰命名法
# input函数， 可以让玩家在控制台输入自己像输入的值
if (index == 1 and people_num == 3) or (index == 2 and people_num == 1) or (index == 3 and people_num == 2):
    print('您输了!')
elif index == people_num:
    print('平手')
else:
    print('您赢了!')
```

```python
# 2. 1到100相加
# 方法1
total = 0
# 注意for循环和randint不同， for循环为左闭右开区间
for i in range(101):
    total += i
total   # 结果为5050

# 方法2
total = 0
count = 1
while(count <= 100):
    total += count
    count += 1
total  # 结果为5050
```

```python
# 3. 当玩家和电脑平手的时候循环进行游戏
import random

while True:

    index = random.randint(0, 2)  # randint为左闭右闭区间， index可以随机取得0， 1， 2, 在这里我们将它当做电脑的出拳

    people_num = int(input('请出拳：1，剪刀  2，石头  3，布'))

    if (index == 1 and people_num == 3) or (index == 2 and people_num == 1) or (index == 3 and people_num == 2):

        print('您输了!')

    elif index == people_num:

        print('平手, 再来一次')

    else:

        print('您赢了!')

        break  # 执行break将直接跳出循环, 还有continue也可以跳出循环， 但是continue只能跳出本次循环，再去执行下一次循环

print('游戏结束')

```
# 15. 函数

```python
# 函数
def main():
    """
    函数的定义， pass站位可以让这个函数中pass之后的不再执行
    """
    name = 1
    pass  
    print(1)  # 由于前面有pass，所以这句话不再执行
    return name # 结束函数，并返回一个值， 如果在循环中，会有和break相似的效果，且可以直接结束整个函数

if __name__ == '__main':  # 该语句用于判断当前文件是否为主执行程序，是则执行， 不是则不执行, 也可以不进行判断
    main()  # 函数的调用， 如果在最外层的话，可以直接执行
```
```python
# 函数列子
# 函数的列子， 在这里我们通过斐波拉契进行算法进行举例
def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a+b   # 这种写法是python独有的交换两个变量值得方法，非常实用
        print(a)
        
# 函数的列子， 在这里我们通过斐波拉契进行算法进行举例
def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a+b   # 这种写法是python独有的交换两个变量值得方法，非常实用
        return a  # 在不使用return的时候，结果会打印多个值， 但是使用了return，在第一次循环到return的时候，整个函数就结束了，所有只能打印第一个值
        

# 在这个例子中，还有一个更加高级的写法，会使用到yield生成器
def fib_yield(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
        yield a  # 当函数中使用到了yield后， 这个函数会发生变化， 第一次执行函数的时候，他会直接返回一个generator对象,并不会执行函数中的内容
        # 当使用next()函数后(__next__())，会执行一次函数，并返回一个值， 或者使用循环(循环会对generator对象自动调用__next__()方法),
        # 循环输出多个值
        
        
if __name__ == '__main__':
    for a in fib_yield(10):
        print(a)
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(fibonacci(10))
if __name__ == '__main__':
    fibonacci(10)
```
# 16. 嵌套函数

```python
# 嵌套函数：工厂函数
def maker(n):
	def action(x):
        return x ** n
    return action
f = maker(2)  # n = 2
f(3)   # x = 3 结果是3 ** 2

# 嵌套函数： lambda实列
def maker(n):
    action = (lambda x: x ** n)
    return action
f = mark(2)
f(3)   # 结果为3

#-- nonlocal和global语句的区别
# nonlocal应用于一个嵌套的函数的作用域中的一个名称 例如:
start = 100
def tester(start):
    def nested(label):
        nonlocal start             # 指定start为tester函数内的local变量 而不是global变量start
        print(label, start)
        start += 3
    return nested
# global为全局的变量 即def之外的变量
def tester(start):
    def nested(label):
        global start               # 指定start为global变量start
        print(label, start)
        start += 3
    return nested    

```
## 1. 装饰器

把装饰器放在嵌套函数中，是因为我觉得装饰器的实现本质上就是一个嵌套函数。下面用一个简单的例子举例什么是装饰器.

假设，我们一个项目中有一个函数， 我们想要在不改动其原来代码的情况下， 加入一个测试这个方法运行时间的功能， 在这种情况下，我们就可以使用装饰器了

```python
import time


def run_time(func):
    """
    装饰器, 计算一个函数运行的时间
    :return: 装饰好的结果
    """
    def deco(*args, **kwargs):
        """
        装饰的方法， 参数是根据需要装饰的方法的参数而定的，
        如果需要给多个函数进行装饰， 且他们的参数个数不确定，
        可以使用可变参数
        """
        start_time = time.time()
        func(*args, **kwargs)  # 由于此时只是调用了func函数，所以当func有返回值的时候，打印的返回值将为None，要想获得func的返回值，可以使用return func(...)
        print('总共花了：%ss' % (time.time()-start_time))
    return deco


@run_time
def foo():
    """
    我们需要添加装饰器的方法
    计算1到1000的和
    :return: 返回总数
    """
    total = 0
    for i in range(10000000):
        total += i
    print(total)


if __name__ == '__main__':
    foo()

```

和上面差不多的，还有多个装饰器的情况，写法一致， 按照想要的顺序将装饰器写在想要装饰的函数的上面，装饰器是根据顺序执行的。

## 装饰器补充

其实这个部分应该算是函数的补充的，但是在这里介绍的这些知识点，是对理解装饰器比较重要的知识点

### 1) 作用域

在python中， 函数会创建一个新的作用域， 这意味着在函数内部碰到一个变量的时候函数会优先在自己的命名空间里面去寻找，如果找不到，便会往上一层进行查找直到找到为止。下面我将会用一个简单的列子，来展示本地作用域和全局作用域有什么不同

```python
str1 = '我是全局变量'


def foo():
    # 打印当前函数内部变量名称和值的字典
    a = '我是foo函数中的局部变量'
    print(locals())


# 打印Python解释器能看到的变量名称及值的字典
print(globals())  # {..., 'str1': '我是全局变量', 'foo': <function foo at 0x00000238382B1EA0>}
foo()  # {'a': '我是foo函数中的局部变量'}

```

从上面的代码很容易看出来， 在Python解释器，是找不到函数内部自定义的变量的，很好理解的是， 一个是全局变量，而另一个只是局部变量， 所以两个函数之间定义的变量不会相互影响，但是，当我们在一个函数中想要查找一个全局变量的时候，正如上面所说， 他在本地作用域找不到该变量的时候，会接着去上层的作用域查找

```python
str1 = '我是一个全局变量'

def foo():
	print(str1)  # 打印出   我是一个全局变量
```

但是当我们想在函数内部给全局变量赋值，结果可能并不是想的那么简单

```Python
str1 = '我是一个全局变量'


def foo():
    # 在函数内部尝试给一个全局变量赋一个新值
    # 但是其实在函数内部，这种操作其实只是相当于重新定义了一个局部变量
    str1 = '我是一个局部变量'
    print(locals())


foo()  # {'str1': '我是一个局部变量'}

print(str1)  # 我是一个全局变量

# 
```

综合上面的两个程序中，通过运行结果，我们明显可以看到， 函数内部是可以访问到全局变量的，但是却不能给全局变量赋值(当然，像list， dict等这些可变数据类型还是可以进行修改的)  

### 2) 变量生存周期

值得注意的一个点是，变量不仅是生存在一个个的命名空间内， 他们还都有自己的生存周期

```python
def foo():
    x = 1


foo()  # 想要尝试这种方式将foo函数内部的x变量，转到全局来使用
print(x)  # NameError: name 'x' is not defined
```

但是结果并不如我意,  报错的原因很简单，变量x因为某种原因而被销毁了，详细点说： 这不仅仅是因为作用域规则导致的，它还和Python以及其他很多语言中函数调用实现的机制有关。函数foo的命名空间会随着函数调用开始而开始，结束而销毁

### 3) 函数的参数

Python允许我们像函数传递参数, 参数会变成本地变量存在与函数内部。

```python
def foo(x, y):
    """
    x+y
    :param x: 在调用这个函数的时候必须传递x 
    :param y: 在调用这个函数的时候必须传递y
    :return: 返回x， y的和
    """
    return x + y


def foo1(x, y=0):
    """
    同foo
    :param x: 在调用这个函数的时候必须传递x
    :param y: 在给这个函数传递参数是可以不传y, 默认y=0
    :return: x, y的和
    """
    return x + y


def foo2(x=1, y=1):
    """
    同foo
    :param x: 在给这个函数传递参数是可以不传x, 默认y=1
    :param y: 在给这个函数传递参数是可以不传y, 默认y=1
    :return: x, y的和
    """
    return x + y


print(foo(1, 1))  # 2
print(foo1(1))  # 1
print(foo2())  # 2 
```



# 17. 函数补充

```python
#-- 函数参数，不可变参数通过“值”传递，可变参数通过“引用”传递
    def f(a, b, c): print(a, b, c)
    f(1, 2, 3)                         # 参数位置匹配
    f(1, c = 3, b = 2)                 # 参数关键字匹配
    def f(a, b=1, c=2): print(a, b, c)
    f(1)                               # 默认参数匹配
    f(1, 2)                            # 默认参数匹配
    f(a = 1, c = 3)                    # 关键字参数和默认参数的混合
    # Keyword-Only参数:出现在*args之后 必须用关键字进行匹配
    def keyOnly(a, *b, c): print('')   # c就为keyword-only匹配 必须使用关键字c = value匹配
    def keyOnly(a, *, b, c): ......    # b c为keyword-only匹配 必须使用关键字匹配
    def keyOnly(a, *, b = 1): ......   # b有默认值 或者省略 或者使用关键字参数b = value
 
#-- 可变参数匹配: * 和 **
    def f(*args): print(args)          # 在元组中收集不匹配的位置参数
    f(1, 2, 3)                         # 输出(1, 2, 3)
    def f(**args): print(args)         # 在字典中收集不匹配的关键字参数
    f(a = 1, b = 2)                    # 输出{'a':1, 'b':2}
    def f(a, *b, **c): print(a, b, c)  # 两者混合使用
    f(1, 2, 3, x=4, y=5)               # 输出1, (2, 3), {'x':4, 'y':5}
    
#-- 函数调用时的参数解包: * 和 ** 分别解包元组和字典
    func(1, *(2, 3))  <==>  func(1, 2, 3)
    func(1, **{'c':3, 'b':2})  <==>  func(1, b = 2, c = 3)
    func(1, *(2, 3), **{'c':3, 'b':2})  <==>  func(1, 2, 3, b = 2, c = 3)
    
#-- 函数属性:(自己定义的)函数可以添加属性
    def func():.....
    func.count = 1                     # 自定义函数添加属性
    print.count = 1                    # Error 内置函数不可以添加属性
    
#-- 函数注解: 编写在def头部行 主要用于说明参数范围、参数类型、返回值类型等
    def func(a:'spam', b:(1, 10), c:float) -> int :
        print(a, b, c)
    func.__annotations__               # {'c':<class 'float'>, 'b':(1, 10), 'a':'spam', 'return':<class 'int'>}
    # 编写注解的同时 还是可以使用函数默认值 并且注解的位置位于=号的前边
    def func(a:'spam'='a', b:(1, 10)=2, c:float=3) -> int :
        print(a, b, c)
 
#-- 匿名函数:lambda
    f = lambda x, y, z : x + y + z     # 普通匿名函数，使用方法f(1, 2, 3)
    f = lambda x = 1, y = 1: x + y     # 带默认参数的lambda函数
    def action(x):                     # 嵌套lambda函数
        return (lambda y : x + y)
    f = lambda: a if xxx() else b      # 无参数的lambda函数，使用方法f()
 
#-- lambda函数与map filter reduce函数的结合
    list(map((lambda x: x + 1), [1, 2, 3]))              # [2, 3, 4]
    list(filter((lambda x: x > 0), range(-4, 5)))        # [1, 2, 3, 4]
    functools.reduce((lambda x, y: x + y), [1, 2, 3])    # 6
    functools.reduce((lambda x, y: x * y), [2, 3, 4])    # 24
    
#-- 生成器函数:yield VS return
    def gensquare(N):
        for i in range(N):
            yield i** 2                # 状态挂起 可以恢复到此时的状态
    for i in gensquare(5):             # 使用方法
        print(i, end = ' ')            # [0, 1, 4, 9, 16]
    x = gensquare(2)                   # x是一个生成对象
    next(x)                            # 等同于x.__next__() 返回0
    next(x)                            # 等同于x.__next__() 返回1
    next(x)                            # 等同于x.__next__() 抛出异常StopIteration
    
#-- 生成器表达式:小括号进行列表解析
    G = (x ** 2 for x in range(3))     # 使用小括号可以创建所需结果的生成器generator object
    next(G), next(G), next(G)          # 和上述中的生成器函数的返回值一致
    #（1）生成器(生成器函数/生成器表达式)是单个迭代对象
    G = (x ** 2 for x in range(4))
    I1 = iter(G)                       # 这里实际上iter(G) = G
    next(I1)                           # 输出0
    next(G)                            # 输出1
    next(I1)                           # 输出4
    #（2）生成器不保留迭代后的结果
    gen = (i for i in range(4))
    2 in gen                           # 返回True
    3 in gen                           # 返回True
    1 in gen                           # 返回False，其实检测2的时候，1已经就不在生成器中了，即1已经被迭代过了，同理2、3也不在了
 
#-- 本地变量是静态检测的
    X = 22                             # 全局变量X的声明和定义
    def test():
        print(X)                       # 如果没有下一语句 则该句合法 打印全局变量X
        X = 88                         # 这一语句使得上一语句非法 因为它使得X变成了本地变量 上一句变成了打印一个未定义的本地变量(局部变量)
        if False:                      # 即使这样的语句 也会把print语句视为非法语句 因为:
            X = 88                     # Python会无视if语句而仍然声明了局部变量X
    def test():                        # 改进
        global X                       # 声明变量X为全局变量
        print(X)                       # 打印全局变量X
        X = 88                         # 改变全局变量X
        
#-- 函数的默认值是在函数定义的时候实例化的 而不是在调用的时候 例子:
    def foo(numbers=[]):               # 这里的[]是可变的
        numbers.append(9)    
        print(numbers)
    foo()                              # first time, like before, [9]
    foo()                              # second time, not like before, [9, 9]
    foo()                              # third time, not like before too, [9, 9, 9]
    # 改进:
    def foo(numbers=None):
        if numbers is None: numbers = []
        numbers.append(9)
        print(numbers)
    # 另外一个例子 参数的默认值为不可变的:
    def foo(count=0):                  # 这里的0是数字, 是不可变的
        count += 1
        print(count)
    foo()                              # 输出1
    foo()                              # 还是输出1
    foo(3)                             # 输出4
    foo()         
# 该部分转自知乎
```



# 18. 递归函数

```python
# 递归调用
def foo(n):
    if n == 1:
        return 1
    return n * foo(n-1)
foo(3)

# 注意， 在使用递归函数的时候，由于递归深度有限， 所以当数据过大的时候， 在这个例子中，当n为10000的时候就会出现超过最大递归深度的error
```



# 19. 文件读写

```python
# 文件读写
# 读操作
file = open('./TXT.txt', 'w')  # open打开文件  r 为读取, w为写入 a为追加， wb, rb, ab对二进制的文件进行读写
file.read()  # 读取整个文件， 可以通过设置[size]，设置想要读取的大小
file.readline()  # 读取一行
file.readlines()  # 把每一行当成一个list成员， 通过list type返回数据
file.readable()  # 是否可读
file.write('你还') # 想要进行写入， 需要在打开文件的时候写好打开方式
file.writelines(seq)
file.writeable()                          # 是否可写
file.close()                              # 关闭文件。
file.flush()                              # 把缓冲区的内容写入硬盘
file.fileno()                             # 返回一个长整型的”文件标签“
file.isatty()                             # 文件是否是一个终端设备文件（unix系统中的）
file.tell()                               # 返回文件操作标记的当前位置，以文件的开头为原点
file.next()                               # 返回下一行，并将文件操作标记位移到下一行。把一个file用于for … in file这样的语句时，就是调用next()函数来实现遍历的。
file.seek(offset[,whence])                # 将文件打开操作标记移到offset的位置。whence为0表示从头开始计算，1表示以当前位置为原点计算。2表示以文件末尾为原点进行计算。
file.seekable()                           # 是否可以seek
file.truncate([size])                     # 把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。
for line in open('data'): 
    print(line)                         # 使用for语句，比较适用于打开比较大的文件
with open('data') as file:
    print(file.readline())              # 使用with语句，可以保证文件关闭
with open('data') as file:
    lines = file.readlines()            # 一次读入文件所有行，并关闭文件
open('f.txt', encoding = 'latin-1')     # Python3.x Unicode文本文件
open('f.bin', 'rb')                     # Python3.x 二进制bytes文件
# 文件对象还有相应的属性：buffer closed encoding errors line_buffering name newlines等
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 在写文件的时候，还可以指定在什么文件夹中
with open('manhua/connan01.jpg', 'wb') as file:
    file.write(data)
# 但是上面的写法，写的是相对路径，且如果相对路径中找不但manhua这个文件夹，会报错，所以可以使用一下方法先行创建一个文件夹
import os
os.mkdir(__filename__)  # 参数事文件的名字, 会在当前路径下创建一个文件夹
```
# 20. 类

本来初衷是想要将python基础部分的只是，全部放在这一篇一口气写完的， 不过由于后面我又开了详细介绍面向对象的坑， 所以在这篇我就将与类相关的知识略过了



# 21. 抽象类与类的继承

略过

# 22. 异常处理

```python
#-- #捕获异常: 
        try:
        except:                               # 捕获所有的异常 等同于except Exception:
        except name:                          # 捕获指定的异常
        except name, value:                   # 捕获指定的异常和额外的数据(实例)
        except (name1, name2):
        except (name1, name2), value:
        except name4 as X:
        else:                                 # 如果没有发生异常
        finally:                              # 总会执行的部分
    # 引发异常: raise子句(raise IndexError)
        raise <instance>                      # raise instance of a class, raise IndexError()
        raise <class>                         # make and raise instance of a class, raise IndexError
        raise                                 # reraise the most recent exception
 
#-- Python3.x中的异常链: raise exception from otherException
    except Exception as X:
        raise IndexError('Bad') from X
        
#-- assert子句: assert <test>, <data>
    assert x < 0, 'x must be negative'
    
#-- with/as环境管理器:作为常见的try/finally用法模式的替代方案
    with expression [as variable], expression [as variable]:
    # 例子:
        with open('test.txt') as myfile:
            for line in myfile: print(line)
    # 等同于:
        myfile = open('test.txt')
        try:
            for line in myfile: print(line)
        finally:
            myfile.close()
 
#-- 用户自定义异常: class Bad(Exception):.....
    """
    Exception超类 / except基类即可捕获到其所有子类
    Exception超类有默认的打印消息和状态 当然也可以定制打印显示:
    """
    class MyBad(Exception):
        def __str__(self):
            return '定制的打印消息'
    try:
        MyBad()
    except MyBad as x:
        print(x)
    
#-- 用户定制异常数据
    class FormatError(Exception):
        def __init__(self, line ,file):
            self.line = line
            self.file = file
    try:
        raise FormatError(42, 'test.py')
    except FormatError as X:
        print('Error at ', X.file, X.line)
    # 用户定制异常行为(方法):以记录日志为例
    class FormatError(Exception):
        logfile = 'formaterror.txt'
        def __init__(self, line ,file):
            self.line = line
            self.file = file
        def logger(self):
            open(self.logfile, 'a').write('Error at ', self.file, self.line)
    try:
        raise FormatError(42, 'test.py')
    except FormatError as X:
        X.logger()
 
#-- 关于sys.exc_info:允许一个异常处理器获取对最近引发的异常的访问
    try:
        ......
    except:
        # 此时sys.exc_info()返回一个元组(type, value, traceback)
        # type:正在处理的异常的异常类型
        # value:引发的异常的实例
        # traceback:堆栈信息
        
#-- 异常层次
    BaseException
    +-- SystemExit
    +-- KeyboardInterrupt
    +-- GeneratorExit
    +-- Exception
        +-- StopIteration
        +-- ArithmeticError
        +-- AssertionError
        +-- AttributeError
        +-- BufferError
        +-- EOFError
        +-- ImportError
        +-- LookupError
        +-- MemoryError
        +-- NameError
        +-- OSError
        +-- ReferenceError
        +-- RuntimeError
        +-- SyntaxError
        +-- SystemError
        +-- TypeError
        +-- ValueError
        +-- Warning

```
# 23. socket网络编程

```python
# socket 服务端

from socket import socket


server = socket()

# 创建一个服务
server.bind(('127.0.0.1', 6789))
# 监听
server.listen(1024)
print('....服务器已启动，正在监听!...')
while True:
   	# 当未接受到客户端的连接信号， 程序将会在这里阻塞住， 直到有客户端连接进来
    new_client = server.accept()
    print('有客户端连接')
    
# client客户端
from socket import socket

client = socket()
client.connect(('127.0.0.1', 6789))
```
# 24. 多进程

## 1）什么是进程?

一个程序的执行实例就是一个**进程**。每一个进程提供执行程序所需的所有资源。（进程本质上是资源的集合）

一个进程有一个虚拟的地址空间、可执行的代码、操作系统的接口、安全的上下文（记录启动该进程的用户和权限等等）、唯一的进程ID、环境变量、优先级类、最小和最大的工作空间（内存空间），还要有至少一个线程。

每一个进程启动时都会最先产生一个线程，即主线程。然后主线程会再创建其他的子线程。

## 2) 多进程

在linux中， 每个进程都是由父进程提供的， 每启动一个子进程就从父进程克隆一份数据， 但是进程之间的数据本身是不能共享的。

```python
from multiprocessing import Process
import time


def f(name):
    time.sleep(2)
    print('hello', name)


if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
```

```python
from multiprocessing import Process
import os


def info(title):
    print(title)
    print('modul name', __name__)
    print('parent process: ', os.getppid())  # 打印父进程的id
    print('process id: ', os.getpid())  # 获取自己进程的id
    print('\n\n')


def f(name):
    info('进程开始')
    print('hello', name)


if __name__ == '__main__':
    info('你好')
    p = Process(target=f, args=('bob', ))
    p.start()
    p.join()  # 等待子进程执行完毕
# 输出结果

你好
modul name __main__
parent process:  21292
process id:  11392



进程开始
modul name __mp_main__
parent process:  11392
process id:  19032



hello bob
```

## 3) 进程间的通信

由于进程之间的数据是不可共享的， 所以不会出现多线程GIL带来的问题。多进程之间的通信通过Queue()或Pipe()来实现

### a. Queue()

Queue()是实现进程与进程之间通信的一种方法, 他是操作系统开辟的一个空间，可以让各个子进程把信息放大Queue中，也可以把自己需要的信息取走

```python
from multiprocessing import Process, Queue
import os


# 写入进程
def 写入数据(q):
    print('%s开始写入' % os.getpid())
    for i in 'QINGLE':
        q.put(i)
        print('写入: %s' % i)

# 读取数据的进程
def 读取数据(q):
    print('%s开始读取' % os.getpid())
    while True:
        if not q.empty():
            # 从队列中读取信息
            print('读取到数据%s' % q.get())


if __name__ == '__main__':
    q = Queue()
    # 创建写入的进程
    p1 = Process(target=写入数据, args=(q, ))
    p1.start()

    # 创建读取的进程
    p2 = Process(target=读取数据, args=(q,))
    p2.start()
```

注意， 上面的代码中我使用了中文作为函数名字， 只是为了展示Python可以使用这种方式为函数命名， 但是不推荐大家使用这种方式

使用Queue()还有一些常用的方法:

- Queue.qsize(): 返回当前队列包含的消息数量
- Queue.empty(): 如果队列为空， 返回True, 反之False
- Queue.full(): 如果队列满了， 返回True， 反之False
- Queue.get(): 获取队列中的一条信息， 然后将其从队列中移除， 可传参超时时长
- Queue.put(): 将一个值添加进队列， 可传参超时时长
- Queue.put_nowait(): 相当于Queue.get(False), 当队列满了时报错: Full

### b. Pipe()

Pipe()是一条进程与进程之间的管道， 一端发送数据， 另一端就可以接受数据， 使用Pipe()会返回两个连接对象， 分别表示管道的两端， 尽管每端都有send()和recv()方法， 但是一端使用了send方法， 另一端只能使用recv()， 反之也如此。如果两端对应的两个进程试图在同一时间的同一端进行读取和写入， 很有可能将损坏管道中的数据

## 4) Manager

上面的Queue()和Pipe()可以实现进程间的数据传输，而通过Manager可以实现进程间数据的共享， Manager()返回的manager对象会通过一个服务进程， 来是其他进程通过代理的方式操作Python对象。

manager对象支持 `list`, `dict`, `Namespace`, `Lock`, `RLock`, `Semaphore`, `BoundedSemaphore`, `Condition`, `Event`, `Barrier`, `Queue`, `Value` ,`Array`. 

## 5) 进程锁(进程同步)

进程锁的作用是数据输出的时候保证不同进程的输出内容在同一块屏幕正常显示， 防止数据乱序的情况

```python
from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()
        

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()
```

## 6) 进程池

由于进程启动的开销比较大， 使用多进程的时候会导致大量内存空间被消耗。为了防止这种情况发生可以使用进程池，(由于启动线程的开销比较小， 所以不需要线程池这种概念， 多线程只会频繁的切换cpu导致系统变慢， 并不会占用过多的内存空间, 但是为了减少线程启动的开销，所以也可以使用队列的方法实现线程池)

进程池中常用方法：

- apply()  同步执行(串行)
- apply_async()  异步执行(并行)
- terminate() 立刻关闭进程池
- join() 主进程等待所有子进程执行完毕。必须在close或terminate()之后
- close() 等待所有进程结束后， 才关闭进程池.  

```python
from multiprocessing import Process, Pool
import time


def foo(i):
    time.sleep(2)
    return i + 100


def bar(arg):
    print('开始执行: ', arg)


if __name__ == '__main__':
    # 设置允许放入进程池的个数
    pool = Pool(processes=5)

    for i in range(10):
        # foo子进程执行完后， 才会执行callback, 且callback由父进程来执行的
        pool.apply_async(func=foo, args=(i, ), callback=bar)
        # 同步执行
        # pool.apply(func=foo, args=(i, ))

    print('end')  # end会在上面的循环执行完毕后立即执行，所以有可能end会提前输出
    pool.close()
    pool.join()  # 主进程等待所有的子进程执行完毕， 注意！必须在close()或terminate之后
    print('True, end')  # 真正结束
"""    
end
开始执行:  100
开始执行:  101
开始执行:  102
开始执行:  103
开始执行:  104
开始执行:  105
开始执行:  106
开始执行:  107
开始执行:  108
开始执行:  109
"""
```

当去进程从池中获取一个进程的时候，如果进程池序列中没有可供使用的进程， 那么程序就会等待， 直到进程池中有可用进程为止。就像上面的程序一样，for循环产生了10个进程， 但是进程池只允许同时放5个进程， 剩下的都被暂时挂起， 并不暂用内存空间， 等前面的五个进程执行完后，再执行剩下的5个进程

# 25. 多线程

## 1 线程常用方法

- start()  线程准备就绪， 等待CPU调度
- setName()    为线程设置名称
- getName()   获取线程名称
- setDaeman(True)    设置为守护线程
- join()   逐个执行每个线程， 执行完毕后继续往下执行
- run()   线程被cpu调度后自动执行线程对象的run方法， 如果想自定义线程类， 直接重写run方法就行了

## 2. 线程的创建方式

### 1）普通方式

```python
from threading import Thread
import time


def run(n):
    print('task', n)
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')
    time.sleep(1)
    print('0s')
    time.sleep(1)


if __name__ == '__main__':
    t1 = Thread(target=run, args=('t1',))
    t2 = Thread(target=run, args=('t2',))
    t1.start()
    t2.start()
    
# 运行结果
task t1
task t2
2s
2s
1s
1s
0s
0s
```

### 2)  重新构造Thread类中的run方法

```python
from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        print('task', self.n)
        time.sleep(1)
        print('2s')
        time.sleep(1)
        print('1s')
        time.sleep(1)
        print('0s')
        time.sleep(1)


if __name__ == '__main__':
    t1 = MyThread('t1')
    t2 = MyThread('t2')
    t1.start()
    t2.start()
    
# 运行结果和普通方法的结果是一致的
# 在进程中也有这种写法.
```

### 3) 计算子线程执行的时间

注意：sleep的时候是不会占用cpu的，在sleep时操作系统会把线程暂时挂起

- join()    等待线程执行完后，再执行其他线程或者主线程
- threading.current_thread()   输出当前线程

```python
from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        print('task', self.n)
        time.sleep(1)
        print('2s')
        time.sleep(1)
        print('1s')
        time.sleep(1)
        print('0s')
        time.sleep(1)


if __name__ == '__main__':
    start_time = time.time()
    t1 = MyThread('t1')
    t2 = MyThread('t2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('花费时间%s' % (time.time()-start_time))
    
"""
task t1
task t2
2s
2s
1s
1s
0s
0s
花费时间4.003691911697388
<_MainThread(MainThread, started 5472)>
"""
```

### 4) 统计当前活跃的线程数

由于主线程比子线程快很多，当主线程执行active_count()时， 其他子线程都还没执行完毕，因此利用主线程统计的活跃的线程数num = sub_num(子线程数量) + 1(主线程本身)

```python
import threading
from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        print('task', self.n)
        time.sleep(0.5)


if __name__ == '__main__':
    start_time = time.time()
    for i in range(3):
        t = MyThread('t' + str(i))
        t.start()
    time.sleep(0.5)
    print(threading.active_count())  # 输出当前线程

```

主线程比子线程慢很多，当主线程执行active_count()， 其他子线程都已经执行完毕， 因此利用主线程统计的活跃数为主线程的数量, 把上面的代码中的暂停时间，增加为1， 输出结果的活跃数就会变成1。

此外Python内部默认会等待最后一个进程执行完毕后再执行exit().

## 3. 守护线程

在这里使用setDaemon(True)把所有的子线程都变成了主线程的守护线程， 因此当主进程结束后，子线程也会随之结束。所以当主线程结束后， 整个程序就退出了

```python
import threading
import time


def run(n):
    print('task', n)
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')


for i in range(3):
    t = threading.Thread(target=run, args=('t-%s' % i, ))
    t.setDaemon(True)  # 把子进程设置为守护线程，必须在start()之前设置
    t.start()

time.sleep(0.5)
print(threading.active_count())  # 输出活跃的线程数
 
"""
task t-0
task t-1
task t-2
4
"""
```

## 4. GIL

GIL的全称是Global Interpreter Lock(全局解释器锁),  GIL是为了数据安全所创建的。当某个线程想要执行， 必须先拿到GIL, 我们可以把GIL看作是通行证, 并且在一个Pyhton进程中，GIL只有一个。拿不到通行证的线程，就不允许进入CPU执行。GIL只在CPyhton解释器中才有，因为CPython调用的是C语言的原生线程,所以他不能直接操作cpu, 只能利用GIL保证同一时间只能有一个线程拿到数据，而在pypy和jpython中没有GIL

也正是因为有全局解释器锁，所以在某些情况下，由于线程的切换会使得多线程的效率低于单线程

```python
import threading
import time

total_list = []


def run_time(func):
    """
    装饰器,计算
    """
    def wrraper(*args, **kwargs):
        start_time = time.time()
        func()
        print('花费时间:%s' % (time.time()-start_time))
    return wrraper


@run_time
def foo():
    """单线程计算"""
    total1 = 0
    for i in range(500000000):
        total1 += i
    print(total1)


def run(s, e):
    total2 = 0
    for i in range(s, e):
        total2 += i
    total_list.append(total2)


if __name__ == '__main__':
    foo()
    start, end, num = 1, 1, 100000000
    t_list = []
    start_time = time.time()
    for i in range(1, 6):
        start = end
        end = num * i + 1
        t = threading.Thread(target=run, args=(start, end))
        t.start()
        t_list.append(t)  # 将所有的线程存放在列表当中

    for t in t_list:
        t.join()  # 循环等待，使得所有子线程结束了在继续进行主线程

    all_total = 0
    for total in total_list:
        all_total += total
    print(all_total)
    print('多线程花费时间：%s' % (time.time()-start_time))

"""
124999999750000000
花费时间:37.6842622756958
125000000250000000
多线程花费时间：48.508971214294434
"""
# 在这种情况下多线程的速度就会比单线程的速度慢很多,这种情况叫做计算密集型， 计算密集型中
# 多进程 > 单线程 > 多线程

# 还有一种情况是，IO密集型， IO密集型多线程的速度更快
```

IO密集型 & 计算密集型

- 所谓IO密集型任务，是指磁盘IO、网络IO占主要的任务，计算量很小。比如请求网页、读写文件等。当然我们在Python中可以利用sleep达到IO密集型任务的目的。
- 所谓计算密集型任务，是指CPU计算占主要的任务，CPU一直处于满负荷状态。比如在一个很大的列表中查找元素（当然这不合理），复杂的加减乘除等。

综合上面的结果, 在IO密集型的情况下可以使用多线程， 当我们想要使用基于CPython编译器环境时，想要利用好多核cpu， 这个时候我们就可以使用多进程， 因为每个进程都有各自独立的GIL，互不影响, 可以真正意义上的实现并行执行

GIL在Python中的版本差异：

1、在python2.x里，GIL的释放逻辑是当前线程遇见`IO操作`或者`ticks计数达到100`时进行释放。（ticks可以看作是python自身的一个计数器，专门做用于GIL，每次释放后归零，这个计数可以通过sys.setcheckinterval 来调整）。而每次释放GIL锁，线程进行锁竞争、切换线程，会消耗资源。并且由于GIL锁存在，python里一个进程永远只能同时执行一个线程(拿到GIL的线程才能执行)，这就是为什么在多核CPU上，python的多线程效率并不高。 

2、在python3.x中，GIL不使用ticks计数，改为使用计时器（执行时间达到阈值后，当前线程释放GIL），这样对CPU密集型程序更加友好，但依然没有解决GIL导致的同一时间只能执行一个线程的问题，所以效率依然不尽如人意。 

**Python多线程的工作过程**r

## 5 线程锁

由于线程之间是进行随机调度的，所以有可能会遇到多个线程同时修改同一个数据的时候，可能会出现数据重复，甚至数据紊乱。例如下面的例子

```Python
import threading
import time


def run(n):
    global num
    num += 1


num = 0
t_obj = []

for i in range(20000):
    t = threading.Thread(target=run, args=(i, ))
    t.start()
    t_obj.append(t)

for t in t_obj:
    t.join()

print(num)

# 很尴尬，在我的电脑上一直没有出现多个线程同时对同一个num进行操作，不过理论上，这种情况是会出现的，
# 在上面的代码中，我们想要在最后输出的num的值是20000， 但是在实际情况下，因为线程不安全，有可能num的值并不是理想值
```

## 6. 互斥锁(mutex)

为了防止上面的情况发生，就出现了互斥锁(Lock)

```python
import threading
import time

lock = threading.Lock()


def run(n):
    lock.acquire()  # 获取锁   
    global num
    num += 1
    lock.release()  # 释放锁


num = 0
t_obj = []

for i in range(600000):
    t = threading.Thread(target=run, args=(i, ))
    t.start()
    t_obj.append(t)

for t in t_obj:
    t.join()

print(num)

# 线程锁的作用是，当多线程争夺锁时，第一个申请到锁的线程，会在执行公共数据的时候，持续阻塞其他线程
# 当第一个线程锁释放时，后续的线程会继续进行争抢锁
```

## 7. 递归锁

RLock的用法和Lock类一样，但RLock支持嵌套， 在多个锁没有释放的时候，一般会使用RLock类

```Python
import threading
import time

lock = threading.RLock()


def run(n):
    lock.acquire()  # 获取锁
    global num
    num += 1
    lock.release()  # 释放锁


num = 0
t_obj = []

for i in range(600000):
    t = threading.Thread(target=run, args=(i, ))
    t.start()
    t_obj.append(t)

for t in t_obj:
    t.join()

print(num)

# 递归锁和互斥锁的区别时，递归锁允许在同一线程中被多次acquire获取, 而互斥锁，顾名思义，他并不允许这种请款发生。但是在递归锁中要注意的是， 他的获取与释放必须成对出现，即获取了多少次，就必须释放多少次
```

## 8. 信号量(BoundedSemaphore类)

互斥锁同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据，等允许的多个线程中的某一个或者多个操作完毕后，后面的人再去填操作完毕的线程留下来的位置，直至填满我们设定的允许的数量的值。就好比，一个厕所只有3个坑位，所以最多允许3个人同时上厕所，后面的人只能等里面有人出来了才能进去

```Python
import threading
import time


semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行


def run(n):
    semaphore.acquire()  # 加锁
    time.sleep(1)
    print('启动线程：%s\n' % n)
    semaphore.release()  # 释放


for i in range(22):
    t = threading.Thread(target=run, args=(i, ))
    t.start()


if threading.active_count() != 1:
    pass

else:
    print('所有线程执行完毕!')

# 其中过程各自体会
```

## 9. 事件(Event类)

python线程的事件用于主线程控制其他线程的执行，事件是一个简单的线程同步对象，其主要提供以下几个方法：

- clear   将flag设置为'False'
- set    将flag设置为'True'
- is_set   判断是否设置了flag
- wait  会一直监听flag, 如果没有检测到flag就一直处于阻塞状态

事件处理的机制：全局定义了一个‘Flag’, 当flag值为'False', 那么event.wait()就会阻塞，当flag值为'True', 那么event.wait()便不再阻塞

```Python
import threading
import time


event = threading.Event()


def lighter():
    count = 0
    event.set()
    while True:
        if 5 < count <= 10:
            event.clear()  # 红灯，清楚标志位
            print('红灯')
        elif count > 10:
            event.set()  # 设置标志位
            count = 0  # 绿灯，设置标志位
        else:
            print('绿灯')
        time.sleep(1)
        count += 1


def car(name):
    while True:
        if event.is_set():  # 判断是否设置了标志位
            print('[%s] 运行中...' % name)
            time.sleep(1)
        else:
            print('[%s] 红灯请稍等...' % name)
            event.wait()  # 等待标志位，如果没有检测到标志位，将会阻塞在这里，无法执行下面的操作
            print('[%s] 绿灯，可以走了')


light = threading.Thread(target=lighter,)
light.start()

car = threading.Thread(target=car, args=('宝马',))
car.start()
```

### 10.条件(Condition类)

使得线程等待，只有满足某条件时，才释放n个线程

### 11.定时器(Timer类)

定时器，指定n秒后执行某操作

```Python
from threading import Timer


def foo():
    print('hello, world!')


t = Timer(1, foo)
t.start()  # 1秒之后执行函数foo

```

## 12 线程池

我们可以使用队列queue.Queue()来实现线程池, 原理是， 我们可以将任务放进队列中去， 然后开多个线程，每个线程都去队列中取一个任务， 执行完了再去获取队列中的下一个任务， 直至队列中所有任务都被取空了， 再退出线程

```Python
from queue import Queue
import time
import threading


queue = Queue()


def foo():
    while True:
        # queue.get(item, block=True, timeout=None)
        # 从队列中获取一个数据， block是是否允许为空，
        # 当block为False的时候, 如果获取到None时，会报错，
        # 当block为True的时候， 如果获取到None时会一直等带队列中有数据
        # timeout为设置超时时间
        i = queue.get()
        time.sleep(1)
        print('index %s, thread: %s' % (i, threading.current_thread()))
        #
        queue.task_done()


if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=foo)
        t.daemon = True  # 设置守护线程， 当主线程结束后，退出该线程
        t.start()

    time.sleep(3)

    for j in range(10):
        queue.put(j)  # 往队列中放数据。和get的参数一样

    # 一直阻塞到队列中的所有元素都被取出和执行
    queue.join()
```





# 26. 协程

协程，又称微线程。在使用时只使用一个线程，协程可以分解一个线程成为多个微线程，并且在该线程中按照规定的某个代码块的执行顺序进行执行。

协程拥有自己的寄存器上下文和栈

协程调度切换时，将寄存器上下文和栈保存到其他地方， 再切换回来的时候，恢复先前保存的寄存器上下文和栈。

所以， 协程能保留上一次调用时的状态(即所有局部状态的一个特定组合), 每当程序切换回来时，就进入上一次离开时程序所处的代码段

综上， 协程的定义就是：

- 须在只有一个单线程里实现并发 
- 修改共享数据不需要加锁
- 用户程序里保存多个控制流的上下文栈
- 一个协程遇到IO操作自动切换到其他协程

在Python中，有很多方法可以实现协程操作， yield/send,  greenlet, gevent,  async/await

## 1. yield/send实现协程

当一个函数中包含了yield语句时， Python会自动将其识别为一个生成器。这个时候，调用这个函数，将返回一个生成器对象, 在前面的斐波拉契序列中，我已经展示过了yield的用法了, 下面再介绍通过yield实现消费者生产者模型

```Python
# 消费者生产者模型的简单概述就是, 生产者生产商品后，消费者消费，当商品没有了，生产者继续生产， 重复整个过程
# 通过这个简单的概述其实多线程也可以实现这个功能，一个线程生成消息 一个线程取得消息，通过锁控制队列和等待，但是使用多线程很有可能会形成死锁
def producer(c):
    """
    生产者,
    """
    # send(value)会将方法中的value发送给生成器c
    c.send(None)  # 第二步，启动生成器 启动生成器的时候value必须为None
    n = 0  # 第4步  消费者通过yield 返回了一个值,
    while n < 5:  # 注意， 由于这里不能使用for循环，目前还不知道什么原因，猜测可能是由于for循环会默认执行__next__()
        n += 1
        print('[生产者]正在生产中')
        r = c.send(n)  # 5 再次使用send发送了一个n值给消费者
        print('[生产者]消费者回馈: %s' % r)
    c.close()


def consumer():
    """消费者"""
    r = ''  # 第三步，由于第一步生产者方法send了一个None, 直接进入消费者方法
    while True:
        # 当生产者第一次发送的时候，其实相当于相当于启动生成器, 所以在第一次的时候，不会直接将值反给yield
        # 当生产者send(value)发送过来一个n值，会返回生成器生成的下一个操作
        # 而value则会变成生成器当前的值，所以在当前项目中当value=1的时候， yield返回的是1, 并执行的下一步操作
        # 在当前项目中，即执行if not n即之后的操作
        n = yield r  # yield返回r并赋值给n
        if not n:
            return
        print('[消费者]正在消费 %s...' % n)
        r = '200 OK'


c = consumer()  # 由于该方法中有yield，所以Python会将其默认为生成器
producer(c)  # 第一步, 执行producer方法
    
```

## 2. greenlet实现协程

```python
# 同样使用上面的消费者生产者模型
from greenlet import greenlet


n = 0


def consumer():
    """消费者"""
    global n
    while n < 5:
        print('消费者消费产品 %s' % n)
        print('消费者回馈')
        gr1.switch()


def producer():
    global n
    while True:
        n += 1
        print('生产者生产产品')
        gr2.switch()  # 将任务切换到消费者方法中
        if n > 5:
            break


gr1 = greenlet(producer)
gr2 = greenlet(consumer)
gr1.switch()  # 将任务切换到gr1 即生产者方法中

# greenlet主要通过switch来切换任务
```

## 3. gevent实现协程

```Python
from gevent import monkey; monkey.patch_all()
import gevent
import requests


def f(url):
    print('爬取: %s' % url)
    req = requests.get(url)
    data = req.text
    print('获取到%s网页一共%d字节的数据' % (url, len(data)))


gevent.joinall([
    gevent.spawn(f, 'https://www.baidu.com'),
    gevent.spawn(f, 'https://blog.csdn.net'),
    gevent.spawn(f, 'https://www.cnblogs.com'),
])   
```



# 27. 异步

上面介绍的线程和进程使用的都是同步机制， 说到同步就不得不说到同步与异步之间的区别:

- 同步  是指完成事务的逻辑， 如果阻塞了， 会一直等待， 直到这个事务完成， 再执行第二个事务， 顺序执行。简单来说就好像是你去书店买书,   但是不知道在哪里， 之后老板告诉你他需要再系统里面查一下书的位置，你可以选择等待老板查完书(**同步阻塞**), 你也可以选择在书店逛一逛，让老板查好了，大声告诉你在哪(**同步非阻塞**)
- 异步  是和同步相对的，异步是指在处理调用这个事务之后，不会等待这个事务的处理结果， 直接处理第二个事务去了,  通过状态通知来通知调用者处理的结果。按照上面的场景解释就是，老板说要去系统查找一下书的位置，等查好了叫店小二帮你找书并拿给你，这个时候你可以选择等待(异步阻塞), 你也可以选择出去转转，最后会有人把书拿给你的(**异步非阻塞**)

下面我将使用asyncio来进行几个简单的异步编程

```Python
import time
import asyncio


# 在定义函数时在def前面加上一个async，这个函数就成了异步函数
async def foo():
    # 休眠一秒种， 和time.sleep()相似， 使用asyncio.sleep()可以有异步非阻塞效果，
    # 但是如果将asyncio.sleep更改成time.sleep()，就会变成异步阻塞，
    # 所以当foo函数在休眠时期会直接进行其他操作
    asyncio.sleep(1)
    print('hello, world, 现在的时间戳为: %s' % time.time())


def run():
    for i in range(5):
        # run_until_complete(future)方法的作用是，运行future直到结束
        loop.run_until_complete(foo())


# 返回一个异步事件循环
loop = asyncio.get_event_loop()
if __name__ == '__main__':
    run()
    
"""
运行后会发现，虽然这个程序使用asyncio添加了休眠时间，
但是由于异步非阻塞的问题，当事件循环遇到本应阻塞的情况下，直接去执行下一个操作
所以运行结果几乎是同时出来，且速度极快
"""
```

```Python
# 这里会使用到async/await来实现异步编程
import time
import asyncio
from aiohttp import ClientSession


tasks = []
start_urls = [
    'https://blog.csdn.net/zoe9698/article/details/74351925',
    'https://www.cnblogs.com/rockwall/p/5750900.html',
    'https://www.baidu.com',
    'https://docs.python.org'
]


async def foo(url):
    """
    使用async关键字，将该方法变成异步函数
    :param url: 想要访问的url
    """
    # ClientSession 用于做Http请求的第一类接口
    async with ClientSession() as session:
        # get方法，执行http获取请求，和requests类似，但这里的
        # get是非阻塞的，如果在这里改用requests的话，或者添加了requests去执行其他的请求任务
        # 程序执行到这儿，会被阻塞
        async with session.get(url) as response:
            response = await  response.read()
            print(len(response))
            print('hello, world: 现在的时间戳为%s' % time.time())


def run():
    for url in start_urls:
        # 创建一个task， .create_task(coroutine)也有这个效果
        task = asyncio.ensure_future(foo(url))
        tasks.append(task)


if __name__ == '__main__':
    # 获取异步时间循环
    loop = asyncio.get_event_loop()
    run()
    # wait方法是，等待将来完成的和协程执行完毕
    loop.run_until_complete(asyncio.wait(tasks))

```

