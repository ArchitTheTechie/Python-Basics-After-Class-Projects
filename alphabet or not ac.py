#Making a program to check whether the given characteris an alphabet or not


ch = input("Enter a character: ")

if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
    print("It is an alphabet.")
else:
    print("It is NOT an alphabet.")
