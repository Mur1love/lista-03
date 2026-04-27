from src.my_node import MyNode


def reverse_linked_list(head: MyNode) -> MyNode:
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
