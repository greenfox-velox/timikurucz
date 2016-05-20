# bubble_sort([3,9,4,5,2,1])
# # expected output: [1,2,3,4,5,9]

list = [3,9,4]
new_list = []


def bubble_sort(input):
    for i in range(len(input)):
        for j in range(i+1, len(input)):
            if input[j] < input[i]:
                input[j], input[i] = input[i], input[j]
    return input

print(bubble_sort(list))
