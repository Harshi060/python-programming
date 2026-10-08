1.Using Temporary Variable

a = int(input("Enter a: "))
b = int(input("Enter b: "))

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)

2.Using Arithmetic Operators
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)


3.Using XOR Operator
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:")
print("a =", a)
print("b =", b)
