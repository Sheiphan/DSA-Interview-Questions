class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def reversell(head):
    temp = head
    prev = None

    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front

    return prev


def print_ll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


if __name__ == "__main__":
    arr = [2, 5, 8, 7, 9]

    head = Node(arr[0])

    temp = head
    for i in range(1, len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next

    head = reversell(head)
    print_ll(head)
