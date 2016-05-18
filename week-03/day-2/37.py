numbers = [3, 4, 5, 6, 7]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens

def even_numbers (input):
    new_list = []
    for number in input:
        if number % 2 == 0:
            new_list.append(number)
    return (new_list)

print(even_numbers(numbers))
