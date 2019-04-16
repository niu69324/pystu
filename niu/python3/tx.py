#生成器generator
gt=(x*x for x in range(1,15))
print(gt)
#print(next(gt))
print('============')

for x in gt:
	print(x)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(10))

	
#杨辉三角
def yh(n):
	li=[1]
	index=0
	while index<n:
		yield li
		li=[1]+[li[i] + li[i + 1] for i in range(len(li) - 1)]+[1]
		index+=1
#调用打印
for x in yh(10):
	print(x)
	
