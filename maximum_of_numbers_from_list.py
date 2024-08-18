#find the maximum of three numbers using list
lst = list(map(int, input("Enter Nums : ").split()))
print(lst)

# Initialize the largest number with the first element
largest = lst[0]

# Iterate through the list to find the largest number
for i in lst:
    if i > largest:
        largest = i

print("The largest number is:", largest)



