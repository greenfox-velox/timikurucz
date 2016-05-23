# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    f = open(file_name)
    text_list = f.readlines()
    rev_list = reversed(text_list)
    new = ''
    for item in rev_list:
        new += item
    f.close()
    return new
