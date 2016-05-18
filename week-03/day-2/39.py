names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list

def shortest_element(input):
    shortest = input[0]
    for string in input:
        if len(string) < len(shortest):
            shortest = string
    return shortest

print(shortest_element(names))
