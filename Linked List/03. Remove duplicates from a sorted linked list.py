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

    def removeDuplicate(self):
        current = self.head
        while current.next:
            if current.data == current.next.data:
                next_to_next = current.next.next
                current.next = next_to_next
            else:
                current = current.next

    # print the linked list
    def printList(self):
        temp = self.head
        while temp:
            print(str(temp.data) + " ", end=" ")
            temp = temp.next


# Driver code
llist = LinkedList()
# function calling
llist.insertAtEnd(1)
llist.insertAtEnd(2)
llist.insertAtEnd(2)
llist.insertAtEnd(2)
llist.insertAtEnd(14)
llist.insertAtEnd(16)
print("Original Linked List")
llist.printList()
print("\nAfter the Operation")
llist.removeDuplicate()
llist.printList()
