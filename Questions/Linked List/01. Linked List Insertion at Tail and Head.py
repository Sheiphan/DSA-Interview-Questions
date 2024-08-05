class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # insert at the end of the linked list
    def insertAtEnd(self, new_data):
        # creation of the new node
        new_node = Node(new_data)

        # linked list is empty
        if self.head is None:
            self.head = new_node
            return

        # insertion at the end
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def insertStart(self, newNode):
        # newNode = Node(99)
        current = self.head
        self.head = newNode
        newNode.next = current

    def insertEnd(self, newNode):
        # newNode = Node(100)
        current = self.head
        while current:
            if current.next is None:
                break
            current = current.next
        current.next = newNode

    # print the linked list
    def printList(self):
        temp = self.head
        while temp:
            print(str(temp.data) + " ", end=" ")
            temp = temp.next


## Driver code
llist = LinkedList()
## function calling
llist.insertAtEnd(12)
llist.insertAtEnd(8)
llist.insertAtEnd(9)
llist.insertAtEnd(10)
llist.insertAtEnd(14)
llist.insertAtEnd(16)
print("Original Linked List")
llist.printList()
print("\nAfter the Operation")
llist.insertStart(Node(1))
llist.insertEnd(Node(987))
llist.printList()


# Original Linked List
# 12  8  9  10  14  16
# After the Operation
# 1  12  8  9  10  14  16  987
