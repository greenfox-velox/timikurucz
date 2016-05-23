# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.read()
    f.close()
    char_list = ''
    for i in range(len(text)):
        if text[i] not in ' \n':
            char_list += (chr(ord(text[i])-1))
        else:
            char_list +=(text[i])
    return char_list

#MADE REFACTORING:
# def decrypt(file_name):
#     f = open(file_name)
#     text = f.read()
#     f.close()
#     char_list = []
#     for i in range(len(text)):
#         if text[i] not in ' \n':
#             char_list.append(chr(ord(text[i])-1))
#         else:
#             char_list.append(text[i])
#     char_text = ''
#     for char in char_list:
#         char_text += char
#     return char_text

#FIRST VERSION:
# def decrypt(file_name):
#     f = open(file_name)
#     text = f.read()
#     print (text)
#     f.close()
#     code_list = []
#     for i in range(len(text)):
#         code_list.append(ord(text[i]))
#     for number in range(len(code_list)):
#         if chr(code_list[number]) not in ' \n':
#             code_list[number] -= 1
#     codes = ''
#     for i in code_list:
#         codes += chr(i)
#     return codes
