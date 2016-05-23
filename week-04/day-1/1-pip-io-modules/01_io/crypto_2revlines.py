# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    text_list = f.readlines()
    new_text = ''
    for line in text_list:
        line = line.rstrip()
        rev_line = line[::-1]
        new_text += rev_line + '\n'
    f.close()
    return new_text
