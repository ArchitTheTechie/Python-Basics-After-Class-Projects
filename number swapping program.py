#Making a program to swap numbers to fix the calculation error Tiya had

# Input values
A = int(input("Enter value of A: "))
B = int(input("Enter value of B: "))
C = int(input("Enter value of C: "))

print("Before swapping:")
print("A =", A, "B =", B, "C =", C)

# Swapping (cyclic rotation)
temp = A
A = B
B = C
C = temp

print("After swapping:")
print("A =", A, "B =", B, "C =", C)