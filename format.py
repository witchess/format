#!/usr/bin/env python3
#-*-coding: utf-8 -*-
"""
format的用法
字符串的参数使用{num}来表示，0白哦是第一个参数，1表示第二个参数，以后顺次递加
"""
age = 22
name = 'July'

str1 = '{0} is {1} years old.'.format(name,age)
str2 = '{0} is a girl.'.format(name)
#:.n 表示保留小数后的n位
str3 = '{0:.2%}is a decimal.'.format(1/3)
#使用_来补齐空位
str4 = '{0:_^11} is a 11 length.'.format(name)
#别名替换
str5 = '{first} is as {second}.'.format(first=name,second='Wred')
#:n 占字符空间为n个字符
str6 = 'My name is {0:8}.'.format('Fred')
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
