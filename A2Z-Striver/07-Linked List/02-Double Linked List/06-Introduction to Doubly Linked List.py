# Node of a doubly linked list
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        # reference to next node in DLL
        self.next = next
        # reference to previous node in DLL
        self.prev = prev


def ConvertArr2DLL(arr):
    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i], None, prev)
        prev.next = temp
        prev = temp
    return head


def printDLL(head):
    temp = head
    while temp is not None:
        print(temp.data)
        temp = temp.next


arr = [12, 4, 7, 9]
head = ConvertArr2DLL(arr)
print(printDLL(head))
