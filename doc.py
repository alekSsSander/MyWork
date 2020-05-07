z= input()
c= z.split()
a= c[0]
b= c[1]
if a > b:
	print('more ' + a)
elif a == b:
	print(a + ' = ' + b)
else:
	print('more ' + b)
