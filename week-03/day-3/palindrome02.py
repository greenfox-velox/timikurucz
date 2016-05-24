# Create a function that searches for all the palindromes in a string that are at least than 3 characters, and returns a list with the found palindromes. Example:
# output = search_palindromes('dog goat dad duck doodle never')
# print(output) # it prints: ['dad', 'dood', 'eve']

def is_there_palindromes(input):
    length = len(input)
    palindromes_list = []
    for i in range (0, (length-1)):
        for x in range ((i+3), (length+1)):
            if (input[i:x]) == (input[i:x])[::-1]:
                palindromes_list.append(input[i:x])
    return palindromes_list

print(is_there_palindromes('dog goat dad duck doodle never'))


# sentence = 'mom and dad sit in a kayak'
# def is_there_palindromes(input):
#     length = len(input)
#     palindromes_list = []
#     for i in range (0, (length-1)):
#         for x in range ((i+3), (length+1)):
#             if input[i:x] == input[i:x][::-1]:
#                 palindromes_list.append(input[i:x])
#     return palindromes_list
# print(is_there_palindromes(sentence))
