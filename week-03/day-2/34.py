numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function

def summa (numbers):
    total = 0
    for i in numbers:
        total += i
    return total

print(summa(numbers))
