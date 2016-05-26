# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def char_change(input):
    if len(input) <= 1:
        if input[0] == 'x':
            return 'y'
        else:
            return input
    else:
        if input[0] == 'x':
            return 'y' + char_change(input[1:])
        else:
            return input[0] + char_change(input[1:])

print(char_change('kjjgfxhX'))


# text = 'kjjgfxhX'
# new_text = ''
# for i in range(len(text)):
#     if text[i] == 'x':
#         new_text += 'y'
#     else:
#         new_text += (text[i])
# print(new_text)
