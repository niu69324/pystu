#函数式编程
#高阶函数

#以求绝对值函数为例 abs()

#调用函数
print(abs(-22))
#只打印abs函数名,abs函数本身
print(abs)
#<built-in function abs>

#变量可以指向函数
f=abs
print(f(-24))

#把函数指向变量
#abs=10
#print(abs)
#print()



#传入函数,函数可以当作参数,传入到另外一个函数中
def prin_sum(x,y,f):
	return f(x)+f(y)
#此处犯了一个错误,上面把abs指向了变量10,未注释掉。下面再把abs当作函数传入prin_sum函数中,提示类型错误,因为此时abs函数=10 
print(prin_sum(-10,5,abs))


#python内置函数 map(),reduce() 函数
#map()  接受两个参数,一个是函数,一个是Iterable，map将传入得函数依次作用于序列得每个元素.并把结果作为一个新得iterator返回,使用方法如下
def fu1(x):
	return x*x
	
lz=list(map(fu1,[1,2,3,4,5,6,7,8]))
print(lz)

#reduce()  传入得函数必须接收两个参数。reduce把结果继续和序列得下一个元素做累计计算



#练习,将有问题得英文名字,首字母大写,其它字母小写。使用 upper大写转换 lower 小写转换
def mo_name(name):
	s=name[0].upper()+name[1:].lower()
	return s
names=list(map(mo_name,['lisi','MAY','HSHssgs','alIN','maRRY']))
print(names)
