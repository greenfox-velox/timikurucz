# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Stack ():
    def __init__(self):
        self.element_list = []
    def size(self):
        elements_number = 0
        for number in (self.element_list):
            elements_number += 1
        return elements_number
    def push(self, element):
        (self.element_list) += [element]
    def pop(self):
        new_list = []
        for i in range(0, (self.size()-2)):
            new_list += [(self.element_list[i])]
        last_element = self.element_list[-1]
        self.element_list = new_list
        return(last_element)

test1 = Stack()
test1.push(2)
test1.push(3)
test1.push(4)
test1.push(4)
test1.push(4)
test1.push(4)
test1.push(4)
test1.push(4)
test1.push('kutya')

print(test1.size())
print(test1.element_list)

test1.pop()
print(test1.element_list)
print (test1.pop())
