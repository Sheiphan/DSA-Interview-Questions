class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


# Function to delete the tail of the linked list
def delete_tail(head):
    # Check if the linked list is empty or has only one node
    if head is None or head.next is None:
        return None

    # Create a temporary pointer for traversal
    temp = head

    # Traverse the list until the second-to-last node
    while temp.next.next is not None:
        temp = temp.next

    # Nullify the connection from the second-to-last node to delete the last node
    temp.next = None

    # Return the updated head of the linked list
    return head


# delete the head
def delete_head(head):
    if head is None:
        return head

    head = head.next

    return head


# delete Kth element
def delete_K_Node(k):
    count = 1
    prev = None
    temp = head

    while temp is not None:
        if count == k:
            prev.next = prev.next.next
            break
        prev = temp
        temp = temp.next
        count += 1


# delete the element
def delete_Node(node):
    prev = None
    temp = head

    while temp is not None:
        if temp.data == node:
            prev.next = prev.next.next
            break
        prev = temp
        temp = temp.next


# Function to print the linked list
def print_ll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


# Main function
if __name__ == "__main__":
    # Initialize an array with integer values
    arr = [2, 5, 8, 7, 9]

    # Create the linked list with nodes initialized with array values
    head = Node(arr[0])

    temp = head
    for i in range(1, len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next

    print(f"Original LL: {arr}")

    # Delete the tail of the linked list
    # head = delete_tail(head)

    # head = delete_head(head)
    delete_K_Node(3)
    # delete_Node(7)

    # Print the modified linked list
    print_ll(head)
