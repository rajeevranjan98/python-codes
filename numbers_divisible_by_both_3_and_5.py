#prints all numbers from 1 to 100 that are divisible by both 3 and 5.
#Method-1
a=int(input("Enter First Number :"))
b=int(input("Enter Last Number :"))
for num in range(a, b+1):
	if(num%3==0) and (num%5==0):
		  print(f"{num} is divisible by 3 and 5. ")


print() #For adding NewLine 

#Method-2
# Collect numbers divisible by both 3 and 5 in a list
nums = [num for num in range(a, b+1) if num % 3 == 0 and num % 5 == 0]
# Print the numbers in a single line
print("Numbers divisible by both 3 and 5 are",   *nums)

		
	
	





