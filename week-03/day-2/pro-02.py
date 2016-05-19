# Implement union method which combines two arrays.
#
# union([4,5,6], [1,2,3])
# # expected output: [4,5,6,1,2,3]
#
# union([4,5,7], [4,1,7])
# # expected output: [1,4,5,7]

#FOR LOOP
list_1 = [4,5,6]
list_2 = [1,2,3,6,6]

list_all = list_1 + list_2
new_list = []
for number in list_all :
    if number not in new_list:
        new_list.append(number)
print (new_list)

#FUNCTION
def union (list1, list2):
    list_all = list1 + list2
    new_list = []
    for number in list_all :
        if number not in new_list:
            new_list.append(number)
    return new_list

print (union([4,5,6], [1,2,3]))
print (union([4,5,7], [4,1,7]))
