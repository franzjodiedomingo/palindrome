# check if the number entered is a palindrome
# using def function and if-else 

def palindrome(num):
    return str (num) == str(num) [::-1]

number = 121
if palindrome(number):
    print(f"{number} is a  palindrome")