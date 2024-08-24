# Node class to represent a linked list node
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Function to print the linked list
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print("\n")


# Function to insert a new node at the head of the linked list
def insertHead(head, val):
    temp = Node(val, head)
    return temp


def insert_tail(head, val):
    temp = head

    while temp.next is not None:
        temp = temp.next

    newNode = Node(val)

    temp.next = newNode


def insert_at_k(head, k, val):
    count = 1
    temp = head
    
    if k == 1:
        return Node(val,head)
        
    while temp:
        if count == k-1:
            newNode = Node(val)
            newNode.next = temp.next
            temp.next = newNode
            break
        temp = temp.next
        count += 1
    return head


if __name__ == "__main__":
    # Sample array and value for insertion
    for i in range(7):
        arr = [12, 8, 5, 7]
        val = 100

        # Creating a linked list with initial elements from the array
        head = Node(arr[0])
        head.next = Node(arr[1])
        head.next.next = Node(arr[2])
        head.next.next.next = Node(arr[3])

        # Inserting a new node at the head of the linked list
        # head = insertHead(head, val)

        head = insert_at_k(head, i, 10)

        # Printing the linked list
        printLL(head)
