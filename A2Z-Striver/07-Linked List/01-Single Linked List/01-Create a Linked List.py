class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


# Creating a new Node with the value from the array
y = Node(2)
# Printing the data stored in the Node
print(y.data)


class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


# Creating a Node 'x' with the first element of the array
x = Node(2)
# Creating a reference 'y' pointing to the same Node 'x'
y = x
# Printing the reference 'y', which represents the memory address of the Node 'x'
print(y)
