my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 1
while  i < len (my_nums):
    print (my_nums[i])
    i +=2


x = len(my_nums) - 1
while x >= 0:
    print (my_nums[x])
    x -= 1


y = len(my_nums) - 2
while y >= 0:
    print (my_nums[y])
    y -= 2


z = 0
total = 0
while z < len(my_nums):
    total += my_nums[z]
    z += 2
print (total)


is_there_6 = 0
if 6 in my_nums:
    is_there_6 = True
else:
    is_there_6 = False
print (is_there_6)


f = 0
is_there = False
while f < len(my_nums):
    if 6 == my_nums[f]:
        is_there = True
        break
    f += 1
print (is_there)
