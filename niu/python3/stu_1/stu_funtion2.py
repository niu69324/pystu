#高阶函数
#python 内建函数filter() 也是接收一个函数和一个序列。与map不同的是,把传入的函数依次作用于每个元素,根据返回值的True or False 决定保留还是丢弃该元素
#例:求一个列表中的奇数
def is_odd(n):
	return n%2==1

l0=list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10,11,12]))
print(l0)

#例:删空字符串
def is_del(s):
	#该句的理解为, and ,
	return s and s.strip()

s1=list(filter(is_del,['sw',' ','nx','',None,'a','c']))
print(s1)

#例:用python求回数
#思考, 12321 ,909 808 等之类的数字称之为回数。从正向读和反向读都是一样的

def is_palindrome(n):
	return n == int(str(n)[::-1]) 	#切片的方式 str(n)[::-1] 将n转换为字符串,忽略起止位置
	
print(is_palindrome(3333))
sx=list(filter(is_palindrome,[222,123,234432,3234312,1234321,5445,999]))
print(sx)
	
