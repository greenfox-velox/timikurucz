sentence = 'mom and dad sit in a kayak'
words_list = sentence.split(' ')

length = len(words_list)
palindromes_list = []

def is_there_palindromes(input):
    length = len(input)
    palindromes_list = []
    for word in words_list:
        if len(word) >= 3:
            for i in range (0, (len(word)-1)):
                for x in range ((i+3), len(word)+1):
                    if word[i:x] == word[i:x][::-1]:
                        palindromes_list.append(word[i:x])
    return palindromes_list
print(is_there_palindromes(words_list))
