#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/5/19 9:06
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司

'''
一段可以实现特定功能的代码--封装成函数。---提高代码的复用率
def  函数名称():
    函数体(实现功能的代码段)
1、定义的函数，必须要调用，才会执行；不调用不会执行  --- 如何调用函数？ ==函数名调用
2、debug-调试--断点 ？？
3、优化：可能会变化的变量-- 定义成为函数的参数 --- 传入参数

定义参数的类型：
1、必备参数 ：定义了必须要传入，不传入报错
2、默认参数（缺省参数）：定义的时候赋值一个默认值，可以不传入--默认值； 也可以传入--用传入的值替换默认值；--必须在必备参数后面
3、不定长参数： --不确定长度
*args : 当前面的必备参数和默认参数都接收完了之后，剩下的参数都会被这个不定长的参数接收，并以元组的格式保存的；== 位置传参
--- 可以传入，也可以不传入，可以传入1个 ，多个 --灵活
**kwargs: 当前面的必备参数和默认参数都接收完了之后，剩下的参数都会被这个不定长的参数接收，并以字典的格式保存的 =关键字传参

参数传入三种方式：
1、位置传参： 安装参数的位置，以此传入参数  -- 位置
2、关键字传参：指定参数名 进行参数的传入，更加准确-- 位置不相关了。
3、混合传入：结合位置、关键字传入参数：
注意：关键字传入在位置传参的后面！！

函数返回值：
1、 函数默认没有返回值--- None（空）
2、定义函数的返回值：
使用场景： 函数的有一个值是想要给调用的人去用-- 定义成返回值  -- 调用函数就可以直接得到返回值
3、返回值可以定义一个，定义多个,中间用逗号隔开； 接收- 元组的形式保存
4、函数返回值表示着函数执行的结束 -- 一定放最后
'''
def Good_job(salary,bonus,subsidy=500,*args,**kwargs):  # 定义函数的参数 === 形参
    sum1 = salary + bonus + subsidy
    print('参数salary：{}'.format(salary))
    print('参数bonus：{}'.format(bonus))
    print('参数subsidy：{}'.format(subsidy))
    print('参数args：{}'.format(args))
    print('参数kwargs：{}'.format(kwargs))
    for i in args:   # 遍历元组
        sum1 += i
    for j in kwargs:   # 遍历字典
        # sum1 += kwargs.get(j)   # 字典取值--key对应的value
        sum1 += kwargs[j]
    print('这个工作的工资总和是：{}'.format(sum1))
    return sum1,salary   # 把这个工资总和变量 --定义成返回值====执行结束，后面的语句都不会再执行
    print("6666")

result = Good_job(8000,2000,800,100,200,300,400,a=111,b=222,c=333,d=444)  # 函数的调用 -- 传入参数  == 实参
print(result)
# if  result > 10000:
#     print('工作是个不错的工作！')
# else:
#     print("工作工资不ok！")
'''
内置函数：
print()
type()
isintance()
len()
str(),int(),float(),bool(),list(),tuple(),set(),dict()
range()
input()
字符串，列表 字典 元组 内置方法
.format()
'''
dict1 = {"name":"运",'age':"18"}
dict2 = dict(name='look-on',age=18)
print(dict1)
print(dict2)

