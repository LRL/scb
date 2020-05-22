#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/5/19 13:26
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司

'''
Python第三方库：别人用代码已经编写好的一组功能，我们要用的话 直接用--- pip--安装Python第三方库的工具：在线下载，自动安装
1、安装 ：requests 库 ，  pip install requests
2、导入：import requests

requests库功能： 发送http接口请求
http协议： 应用层协议
请求消息：请求行，请求头，空一行，请求数据
响应消息：状态行，响应头，空一行，响应正文
   状态码： 200 ok ，404 500 503 403 302

1、返回的页面有乱码 --指定解码方式
2、页面内容不对 ： 百度服务器安全机制--反爬虫机制： 机器发过来请求（不是真实浏览器的正常请求）--不会给你返回正常页面！
请求头部：User-Agent:
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36
注意：requests库传参数： 除了URL之外，其他的参数都必须要用 字典 的格式 传输 ！！！
'''
import requests  # 导入requests库--当前Python文件有效
def baidu_get():
      baidu_url = "https://www.baidu.com/"  # 定义个百度的URL
      baidu_headers = {'User-Agent':
                             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
      response = requests.get(baidu_url,headers=baidu_headers)  # 调用函数-传入必备参数== 接收函数返回值
      # print(response.text)  # text--直接去获取页面内容，自动解码  -- 80%
      html = response.content.decode('utf8') # 指定解码方式页面解码
      print(html)

'''
get请求 ： 参数-- url
post请求： 参数--请求体 
https://www.baidu.com/s?wd=柠檬班
协议：//域名&IP：端口/资源路径?参数名=参数值&参数2名=参数2值
http://www.lemfix.com/search?q=git
'''
baidu_url = "http://www.lemfix.com/search"
baidu_headers = {'User-Agent':
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
baidu_param = {'q':"git"}  # 定义请求带的参数
response = requests.get(baidu_url,params=baidu_param,headers=baidu_headers)  # 发送带参数的请求
html = response.content.decode('utf8')  # 指定解码方式页面解码
# print(html)

# post 前程贷接口：--接口文档
# '{"status":0,"code":"20110","data":null,"msg":"手机号码已被注册"}'
# {"status":1,"code":"10001","data":null,"msg":"登录成功"}

qcd_url = "http://test.lemonban.com/futureloan/mvc/api/member/register"   # 接口地址
qcd_data = {"mobilephone":"13788996677",'pwd':'12345678'}  # 参数
res = requests.post(url=qcd_url,data=qcd_data)  # post方法发送接口请求
result = res.text   # 字符串--文本
result1 = res.json()   # 用json获取响应结果  -- 字典格式
print(type(result1))

result = result.replace("null",'None')   # 字符串替换文本
result  = eval(result)   # 字符串转化为字典
print(type(result))
print(result.get("msg"))  # 字典取值

'''
eval函数  --  运行字符串里边的Python表达式： 
replace函数： 字符串的替换文本的函数
'''

