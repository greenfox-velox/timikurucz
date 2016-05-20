# We want to know the index of the vowels in a given word, for example, there are two vowels in the word super (the second and fourth letters).
# So given a string "super", we should return a list of [2, 4].


def vowel_indices(word):
    vowels = ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'I', 'E', 'O', 'U', 'Y')
    index_list = []
    index = 1
    for char in word:
        if char in vowels:
            index_list.append(index)
        index += 1
    return index_list


print(vowel_indices('Mmmm')) #=> []
print(vowel_indices('Super')) #=> [2,4]
print(vowel_indices('Apple')) #=> [1,5]
print(vowel_indices('YoMama')) #-> [1,2,4,6]
