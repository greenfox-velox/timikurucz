# valtozo = 'pear'

# y = len(valtozo)- 1
# word = ''
# while y >= 0:
#     word += valtozo[y]
#     y -= 1
# print (word)


def make_palindrome(input):
    length = len(input)
    reverse = ''
    for i in range((length-1), -1, -1):
        reverse += input[i]
    pal = input + reverse
    return pal

print(make_palindrome('pear'))
