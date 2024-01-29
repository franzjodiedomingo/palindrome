# check if the number entered is a palindrome
# using def function and if-else 

def palindrome(num):
    return str (num) == str(num) [::-1]

number = 198
if palindrome(number):
    print(f"{number} is a  palindrome")
else:
    print(f"{number} is not a palendrome")