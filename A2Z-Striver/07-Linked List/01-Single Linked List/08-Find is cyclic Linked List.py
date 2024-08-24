class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


def detect_cycle(head):
    slow = head
    fast = head
    while fast and fast.next and slow:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


if __name__ == "__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    # Create a loop
    sixth.next = third

    detect_cycle(head)
