#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#常用的几种参数

#1.必选参数,调用函数时,传入的值按照位置和顺序依次赋值给x和n
def jsuan(x,n):
	sum=1
	while n>0:
		n=n-1
		sum=sum*x
	return sum

print(jsuan(5,3))

#2.默认参数, 
#必选参数在前,默认参数在后
def student(name,age,):
	
  
