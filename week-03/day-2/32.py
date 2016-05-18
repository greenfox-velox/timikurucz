af = 123
# create a function that doubles it's input
# double af with it

def double (input):
    input *= 2
    return input

print (double(af))

#refactoring
def double (input):
    return input * 2
print (double(af))
