class Node:
    def __init__(self, data, next_data=None, prev_data=None):
        self.data = data
        self.next = next_data
        self.prev = prev_data


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
    while temp:
        print(temp.data)
        temp = temp.next


def InsertAtTail(head, k):
    temp = head

    while temp.next is not None:
        temp = temp.next

    newNode = Node(k, None, temp)
    temp.next = newNode

    return head


def InsertAtHead(head, k):
    newNode = Node(k, head)
    return newNode


def InsertAtK(head, k, val):
    temp = head
    count = 1

    if k == 1:
        return Node(val, head, None)

    while temp:
        back = temp
        temp = temp.next
        if count == k - 1:
            newNode = Node(val, temp, back)
            back.next = newNode
            if temp:
                temp.prev = newNode
            break
        count += 1
    return head


arr = [12, 4, 5, 7]
head = ConvertArr2DLL(arr)

# printDLL(head)
# InsertAtTail(head, -1)
# head = InsertAtHead(head, 9)
head = InsertAtK(head, 3, 10)

printDLL(head)
