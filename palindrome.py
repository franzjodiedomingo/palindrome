# check if the number entered is a palindrome
# using def function and if-else 

def palindrome(num):
    return str (num) == str(num) [::-1]

number1 = 198
if palindrome(number1):
    print(f"{number1} is a  palindrome")
else:
    print(f"{number1} is not a palendrome")

number2 = 121
if palindrome(number2):
    print(f"{number2} is a  palindrome")
else:
    print(f"{number2} is not a palendrome")