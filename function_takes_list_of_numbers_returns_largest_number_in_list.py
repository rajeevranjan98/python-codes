#function that takes a list of numbers and returns the largest number in the list.

def largest_number(lst):
	largest=lst[0]
	for i in lst:
		if i > largest:
			largest=i
	return largest

n=list(map(int, input("Enter the number : ").split()))
result=largest_number(n)
print(f"largest number in the list {n}  is {result}")




