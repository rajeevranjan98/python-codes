#find the maximum of three numbers
a=int(input("a : "))
b=int(input("b : "))
c=int(input("c : "))

if (a>b):
	if(a>c):
		print(f"Max Num in {a}, {b}, {c} :", a)
if(b>c):
	if(b>a):
		print(f"Max Num in {a}, {b}, {c} :", b)
if(c>a):
	if(c>b):
		print(f"Max Num in {a}, {b}, {c} :", c)

