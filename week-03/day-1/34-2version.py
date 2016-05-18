ag = [3, 4, 5, 6, 7]
# please double all the elements of the list
# we want: [3, 4, 5, 6, 7, 3, 4, 5, 6, 7]


i = 0
lenag = len(ag)

# while i < lenag:
#     print (ag[i])
#     ag += [ag[i]]
#     i += 1
# print (ag)



for i in range (lenag):
    print (ag[i])
    ag += [ag[i]]

print(ag)
