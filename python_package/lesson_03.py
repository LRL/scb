#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/5/18 13:45
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司

# python：列表，字典，元组，集合
'''
列表（list）：[],多个元素之间用逗号隔开
1、元素可以是任意数据类型：整型（int），浮点型（float），布尔型，字符串，列表....
2、取值: 也可以通过索引取值，从0开始
   取多个值：切片
3、 列表额元素可以被改变的！！ 增删改操作
增加：append   insert
删除：
修改
4、列表元素是可以重复的：count
5、列表有多个元素，统计长度： len()

'''
list1 = [20,3.14,True,"夜",[1,2,3,4,5]] # 空列表,取名字不要用 list()，str(), int()
# print(type(list1))
# print(isinstance(list1,list))  # 判断数据类型 是不是 某一个类型（列表）
# print(list1[-1][1])  # 列表取值的嵌套--扩展
#增加
# list1.append("Mr.Du") # 追加元素到列表末尾
# list1.insert(4,"麦子") # 指定位置添加元素
# print(list1)
# #删除
# list1.pop(5)   # 默认删除最后一个元素，也可以指定索引进行元素的删除
# list1.remove(3.14) # 可以指定某个具体的元素进行删除的
# print(list1)
# #修改
# list1[0] = "音乐"  # 重新赋值
# print(list1)
# list1.append('夜')
# print(list1)
# print(list1.count("夜"))  # 元素出现的次数
# list1.remove("夜")  # 当元素出现多次的时候，remove删除--遇到的第一个元素
# print(len(list1))
# list1.clear()  # 清空元素
# print(list1)

'''
元组（tuple）：(),多个元素之间用逗号隔开
1、元素可以是任意数据类型：整型（int），浮点型（float），布尔型，字符串，列表....
2、取值: 也可以通过索引取值，从0开始
   取多个值：切片
3、元组的元素不可以被改变的！！ --没有增删改操作 ： 如果想要改变？?  == 元组和列表可以相互转化 ！
--- 转化数据类型---列表：list()
4、元组元素是可以重复的：count
5、元组有多个元素，统计长度： len()
'''
# tuple1 = ('音乐', '夜', '麦子', 'Mr.Du', '夜')
# print(tuple1)
# list2 = list(tuple1)  # 先进行数据类型转化-- 复制给一个新的变量 list2
# # tuple1[1] = "猹"  # 不支持修改
# print(list2)
# list2.append("猹")
# print(list2)
# tuple2 = tuple(list2)
# print(tuple2)

'''
字典（dict）：{},多个元素之间用逗号隔开： 每一个元素都是一个键值对： key：value
场景：保存某个对象属性： name：内容，年龄：内容，出生地，身高 ，体重
1、key不能重复，唯一的，而且只能不可变化的数据类型（字符串）；value可以使意数据类型：整型（int），浮点型（float），布尔型，字符串，列表....
2、取值: 字典在Python3.6之前额版本，无序的--没有顺序的，所以也就没有索引 --不能通过索引取值
--通过key取value
3、字典的元素：key不可以被改变，value可以变化 ： 可以重新赋值
-对key进行赋值：
1） 如果key存在： 更新value值--修改元素
2）如果key不存在，新增加一对键值对 -- 增加元素
删除：pop（key）
4、字典有多个元素，统计长度： len()
'''
dict1 = {"name":"刚刚","age":18,"height":"180",'weight':160} # 空字典
print(len(dict1))
print(dict1['name'])  # key --value
print(dict1.get('weight'))  # get()- value
print(dict1.items())  # 不做重点掌握
dict1["name"] = "Sugar"   # 修改key对应的value
print(dict1)
dict1["city"] = '北京'
print(dict1)
dict1.pop('weight')  # 无序，没有默认删除 -- 指定对应的key 删除键值对
print(dict1)
dict1.update({'tt':'tt','rr':'rr'})
print(dict1)


'''
集合： set ，{}
1、 元素是不可以重复的
使用场景： 用来给列表进行去重
2、无序的
'''
# list2 = [20,"夜",True,"夜","夜",20,30]
# print(list2)
# # 统计一下列表中不重复的元素： 转化为集合 --set()
# set1 = set(list2)  # 转化为集合-去除
# print(set1)
# list4 = list(set1)
# print(list4)

# 控制流： for循环  ， if判断
'''
if判断：选择--语法
if 条件：（判断这个条件是否成立-如果成立的话-结果布尔值== 只有条件成立的后，才会去执行下面的语句）
    执行语句 （注意： 子代码）
elif 条件： (可以没有，也可由1-多个)
    执行语句
else：
    执行语句  
注意： 只有上面的条件不满足时，才会去执行下面的条件。
'''
# money = int(input("请输入自己的存款余额："))  # 控制台输入的内容--赋值给money 变量  -- 数据类型--字符串
# if money >= 200:  # 条件执行结果== True
#     print('买房买车！巅峰')
# elif money >= 100: # False
#     print('付首付，买房子！')
# elif money >= 50: # True
#     print('买个车，跑滴滴！')
# else:
#     print('滚去工作，学习！！')

'''
For循环：重复执行某一段代码 -- 遍历某个数据类型的所有的元素，逐个进行操作。 == 列表，元组，字符串，字典
--tab  --4个空格缩进
循环结束的标识： 元素都遍历完成了
循环次数 是 元素个数决定的 

'''
# str_1 = "丢丢是最美的"  # 字符串
# for item in str_1:
#     print(item)
#     print("---" * 10)

# list5 = ['Mosaic','柚子','麦子','夜','look-on','脸脸']
# count = 0 # 计数
# for name in list5:
#     print(name)
#     print("--" * 10)
#     count += 1
# print(count)  # 循环次数
# print(len(list5))  # 列表元素的个数

# range函数 ==经常跟for循环一起使用： 用来生成一个整数序列
# 开始 （默认值-0） 结束（必须填） 步长（默认是1）： 1,10,2 == 取头不取尾
for i in range(10):
    print(i)
    if i == 5:
        # continue  # 跳出本次循环，后续的循环继续执行
        break  # 直接跳出循环，后面不再执行



# 作业-- 扩展 input()--Python内置函数： 进行控制输入


