# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    f = open(file_name)
    new = ''
    for line in f:
        for i in range(0, len(line), 2):
            new += line[i]
    f.close()
    return new
