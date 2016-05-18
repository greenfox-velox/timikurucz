ag = [3, 4, 5, 6, 7]
# please double all the elements of the list

b = 0
length_ag = len(ag)

while b < length_ag:
    ag[b] *=2
    b += 1
print (ag)



#2nd solution
ak = [3, 4, 5, 6, 7]
y  = len(ak)
while y > 0:
    ak[y-1] *=2
    y -= 1
print (ak)
