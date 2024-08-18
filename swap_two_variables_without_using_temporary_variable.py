#swap two variables without using a temporary variable.
a=int(input("a : "))
b=int(input("b : "))

a, b=b, a

print("a ", a)
print("b ", b)

