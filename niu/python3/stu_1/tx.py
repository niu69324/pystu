#高级特性
#from collection import Iterable

#切片,取一个list或是tuple的部分元素
#list
names=['ls','admin','shay','sharry','lucy','may']
#tuple
lag=('python','java','c++','c#','php','golang','vb','html')

#取前几个元素,本办法 使用for循环
r=[]
for x in range(3):
	r.append(names[x])

print(r)

#切片操作Slice
#取list中的前三个元素
print(names[0:3])
#从1开始 取两个元素
print(names[1:3])
#取最后一个元素
print(names[-1])
#取倒数两位
print(names[-2:])


#创建0-99的元组
li=list(range(100))
#将元组转换为列表
L=list(li)
print(L)
print(li[88])
#取0-22位
print(L[0:22])
#倒数32至倒数第一位
print(L[-32:])


#使用迭代寻找一个list中的最大和最小值,并返回一个tuple
lis=[11,3,5,61,48,77,5,31,2,0]
def prn_max(list):
	if list==[]:
		return[None,None]
	else:
		min=list[0]
		max=list[0]
		for i in list:
			if min<i:
				min=i
			if max>i:
				max=i
		return(max,min)
		
		
print(prn_max(lis))

#使用迭代,迭代一个字符串
str='hello world'
for ch in str:
	print(ch)
	
#如何判断一个对象是否可迭代collection 模块的Iterable来判断
#isinstance('hello',Iterable)


#循环list的下角标和元素,使用enumerate 函数 可以把list变为 索引-元素 对
for i,value in enumerate(['java','python','c++','php']):
	print(i,value)
	
#同时引用两个变量
for a,b in [(1,2),('a','b'),('ss','dd')]:
	print(a,b)
	
#----------------------------------------
#列表生成式,python内置的列表生成式很强大

LL=list(range(0,11))
print(LL)


LLL=[x*x for x in range(0,11)]
print(LLL)

	

