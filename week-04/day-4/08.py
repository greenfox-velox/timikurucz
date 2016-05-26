# Given a string, compute recursively a new string where all the 'x' chars have been removed.

def char_change(input):
    if len(input) <= 1:
        if input[0] == 'x':
            return ''
        else:
            return input
    else:
        if input[0] == 'x':
            return '' + char_change(input[1:])
        else:
            return input[0] + char_change(input[1:])

print(char_change('kjjgfxhX'))
