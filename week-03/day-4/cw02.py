# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contains any char.

def XO(s):
    num_o = 0
    num_x = 0
    o_letters = ('o', 'O')
    x_letters = ('x', 'X')
    for char in s:
        if char in o_letters:
            num_o += 1
        elif char in x_letters:
            num_x += 1
    if num_o == num_x:
        return True
    else:
        return False


print(XO("ooxx")) # => true
print(XO("xooxx")) # => false
print(XO("ooxXm")) # => true
print(XO("zpzpzpp")) # => true // when no 'x' and 'o' is present should return true
print(XO("zzoo")) # => false
