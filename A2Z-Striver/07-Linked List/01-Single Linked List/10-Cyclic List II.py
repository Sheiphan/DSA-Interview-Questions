class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


def reversell(head):
    temp = head
    prev = None

    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front

    return prev


def detect_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            slow = head
            break
    
    while fast and fast.next:
        if slow == fast:
            return slow
        fast = fast.next
        slow = slow.next
    return None


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

    pos = detect_cycle(head)
    print(pos.data)
