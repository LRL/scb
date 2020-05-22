#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/5/20 13:36
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司

'''
第一次作业：
1. 下面哪些不能作为标识符？
1、find 2、 _num 3、7val 4、add. 5、def 6、pan 7、-print 8、open_file 9、FileName
10、print 11、INPUT 12、ls 13、user^name 14、list1 15、str_
答案：
1、find ----ok
2、_num ----ok
3、7val ----no,不能以数字开头
4、add. ----no,只能由字母,数字或下划线组成,不能包含.
5、def ----no,python关键字/保留字
6、pan ----ok
7、-print ----no,只能由字母,数字或下划线组成
8、open_file ----ok
9、FileName ----ok,一般变量名用蛇形小写,类名用大驼峰,模块名用小驼峰
10、print ----ok,但不推荐,这是python封装的一个函数,用了或导致print()用不了，list  str tuple
11、INPUT ----ok,python区分大小写,input!=INPUT
12、ls ----ok
13、user^name----no,只能由字母,数字或下划线组成
14、list1 ----ok
15、str_ ----ok

第二次作业：
1、输入如下格式（input和print（），格式化输出）

2、现在有字符串：str1 = 'python hello aaa 123123aabb'
    1）、请取出并打印字符串中的'python'。
    2）、请分别判断  'o a'      'he'    'ab'  是否是该字符串中的成员？

第三次作业：
1、a=[1,2,'6','summer'] 请用成员运算符判断 i是否在这个列表里面 -- in
2：dict_1={"class_id":45,'num':20} 请判断班级上课人数是否大于5
注：num表示课堂人数。如果大于5，输出人数。
3、list3 = ['夜','脸脸', '猹', '刚刚', 'Mr.Du', '柚子']，扩充列表当中的每一个值包含：姓名、性别、年龄、城市。
以字典的形式表达，并且把字典都存在新的 list中，最后打印最终的列表。
提示： 手动扩充成字典，然后存放到列表里；存放在列表里面

第四次作业：
2. 完成任意整数序列的相加 -- range()--list() - 生成一个整数序列，里面全是数字。求里面所有数字的和
3. 定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。-

'''
# 第二次作业：
# name = input('请输入名字：')
# age = input('请输入年龄：')
# gender = input('请输入性别：')
# print('''***************************
# 姓名：{}
# 性别：{}
# 年龄：{}
# *******************'''.format(name,gender,age))

# str1 = 'python hello aaa 123123aabb'
# print(str1[0:6])
# print('o a' in str1)
# print('he' in str1)
# print('ab' in str1)

#第三次作业：
# a=[1,2,'6','summer']
# if "i" in a:
#     print("i是成员")
# else:
#     print("不是")

# dict_1={"class_id":45,'num':20}
# num = dict_1.get("num")
# if num > 5:
#     print('班上的人数是：{}'.format(num))
# else:
#     print("班上人数不足5人！")

#手动
list3 = ['夜','脸脸', '猹', '刚刚', 'Mr.Du', '柚子']
# dict1 = {"name":"夜","age":"18","city":"北京","gender":"female"}
# dict2 = {"name":"脸脸","age":"18","city":"北京","gender":"female"}
# dict3 = {"name":"猹","age":"18","city":"北京","gender":"female"}
# dict4 = {"name":"万里依然","age":"18","city":"北京","gender":"female"}
# list4 = [dict1,dict2,dict3,dict4]
# print(list4)
#自动：
# list4 = []
# list2 = [18,19,20,21,22,23]
# list1 = ['Female','Man','Female','man','female','man']
# list5 = ['北京','深圳','北京','北京','长沙','武汉']
# for i in range(6):
#     dict1 = dict(name=list3[i],age=list2[i],sex=list1[i],city=list5[i])
#     list4.append(dict1)
# print(list4)

#第四次作业：
# sum = 0
# for i in range(20):
#     sum += i
# print(sum)
#
def function_len(object):
    # if type(object)==dict or type(object)==list or type(object)== str:
    if isinstance(object,str) or isinstance(object,list) or isinstance(object,dict):
        leng = len(object)
        if leng >=5:
            print("True")
        else:
            print("False")
    else:
        print("数据类型不能计算长度！")
function_len([1,2,3,4,5,6])
