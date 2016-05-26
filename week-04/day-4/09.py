# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def char_separator(input):
    if len(input) <= 1:
        return input
    else:
        return input[0] + '*' + char_separator(input[1:])

print(char_separator('alma'))
