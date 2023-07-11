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

    def splitLinkedList(self):
        current = self.head
        A = None
        B = None
        count = 0
        firstTimeA = 1
        firstTimeB = 1

        while current:
            if count % 2 == 0:
                if firstTimeA == 1:
                    firstTimeA = 0
                    A = current
                    currentA = current
                else:
                    currentA.next = current
                    currentA = current
            else:
                if firstTimeB == 1:
                    firstTimeB = 0
                    B = current
                    currentB = current
                else:
                    currentB.next = current
                    currentB = current

            current = current.next
            count += 1
        return (A)

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
llist.insertAtEnd(4)
llist.insertAtEnd(6)
llist.insertAtEnd(14)
llist.insertAtEnd(16)
print("Original Linked List")
llist.printList()
print("\nAfter the Operation")
llist.splitLinkedList()
llist.printList()
