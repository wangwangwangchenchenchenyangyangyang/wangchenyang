n = int(input())
s = 0
num = 1
for i in range(1,n+1):
	
	for x in range(1,i+1):
		print(x)
		num *= x
	s += num
	num = 1
print(s)
