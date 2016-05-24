# Create a method that decrypts the texts/duplicated_chars.txt

# def decrypt(file_name):
#     f = open(file_name)
#     new = ''
#     for line in f:
#         for i in range(0, len(line), 2):
#             new += line[i]
#     f.close()
#     return new


def decrypt(file_name):
    f = open(file_name)
    input_text_list = f.readlines()
    output_text = ''
    for line in input_text_list:
        for i in range(0, len(line), 2):
            output_text += line[i]
    f.close()
    return output_text
