class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def findMiddle(head):
    slow = head
    fast = head

    while fast and fast.next and slow:
        fast = fast.next.next
        slow = slow.next

    return slow.data


if __name__ == "__main__":
    arr = [2, 5, 8, 7, 9, 10]

    head = Node(arr[0])

    temp = head
    for i in range(1, len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
        
    print(findMiddle(head))