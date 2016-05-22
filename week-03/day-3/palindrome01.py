def create_palindrome(input):
    palindrome = input + input[::-1]
    return palindrome
print(create_palindrome('pear'))
