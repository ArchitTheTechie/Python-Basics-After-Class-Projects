# Simple ASCII Value Checker
char = input("Enter a character: ")

# Check if input is a single character
if len(char) == 1:
    ascii_value = ord(char)
    print(f"The ASCII value of '{char}' is {ascii_value}")
else:
    print("Please enter exactly one character.")
