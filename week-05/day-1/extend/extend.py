
# Adds a and b, returns as result
def add(a, b):
    return a+b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c

# Returns the median value of a list given as param
def median(pool):
    sorted_input = sorted(pool)
    if len(sorted_input) % 2 == 0:
        return ( pool[int(len(sorted_input)/2)-1] + sorted_input[int(len(sorted_input)/2)] ) / 2
    else:
        return sorted_input[int((len(sorted_input) - 1) / 2)]

# Returns true if the param is a vovel
def is_vovel(char):
    if char.lower() in 'áéíóőúűaeioöuü':
        return True
    else:
        False

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    new_string =  ''
    for char in hungarian:
        if is_vovel(char):
            new_string += char+'v'+char
        else:
            new_string += char
    return new_string
