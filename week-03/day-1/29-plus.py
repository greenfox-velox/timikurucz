ab = 123
credits = 100
is_bonus = False
# if credits are at least 50,
# and is_bonus is False decrement ab by 2
# if credits are smaller than 50,
# and is_bonus is False decrement ab by 1
# if is_bonus is True ab should remain the same

if credits >= 50 and is_bonus == False:
    ab -=2
elif credits <50 and is_bonus == False:
    ab -=1
elif is_bonus == True:
    None

print (ab)

# refactor:
if is_bonus == False:
        if credits >= 50:
            ab -=2
        else:
            ab -=1
print (ab)


#2
is_bonus = False
if not is_bonus:
        if credits >= 50:
            ab -=2
        else:
            ab -=1


#3
if is_bonus:
    pass
elif credits >= 50:
    ab -=2
else:
    ab -=1
