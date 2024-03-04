class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next =prev
        prev = current
        current = next_node
    return prev

# helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current =current.next
    print("None")
# Example usage:
if __name__ == "__main__":
    # Creating a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print("Original Linked List:")
    print_linked_list(linked_list)

    # Reversing the linked list
    reversed_list = reverse_linked_list(linked_list)

    print("\nReversed Linked List:")
    print_linked_list(reversed_list)