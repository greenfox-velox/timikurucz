# 1. write a recursive function
# that takes one parameter: n
# and counts down from n

def countdown(n):
    if n <= 0:
        pass
    else:
        print(n)
        countdown(n-1)
countdown(10)


# def count(n):
#     for i in range(n, 0, -1):
#         print(i)
# count(10)

# def concat(n):
#     if n <= 0:
#         return []
#     else:
#         return concat(n-1) + [n]
# print(concat(3))
