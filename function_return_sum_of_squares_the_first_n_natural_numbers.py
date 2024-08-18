#function to return the sum of squares of the first n natural numbers.

def sum_of_squares(num):
	sum=0
	for i in range(1, num+1):
		sum=sum+(i*i)
	return sum

n=int(input("Enter the number : "))
result=sum_of_squares(n)
print(f"sum of squares of the first {n} natural number is {result}")




