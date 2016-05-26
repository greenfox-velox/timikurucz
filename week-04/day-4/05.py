# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).

def ears_count(bunnies_num):
    if bunnies_num < 1:
        return 2
    else:
        return 2 + ears_count(bunnies_num-1)

print(ears_count(3))
