numbers = [7, 5, 8, -1, 2]
# Write a function that returns the minimal element
# in a list (your own min function)

def minimum (input):
    min_num = input[0]
    for number in input:
        if number < min_num:
            min_num = number
    return min_num

print (minimum(numbers))
