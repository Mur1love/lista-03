from src.my_node import MyNode


def remove_duplicates(head: MyNode) -> MyNode:
    curr = head
    while curr is not None:
        runner = curr
        while runner.next is not None:
            if runner.next.value == curr.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr = curr.next
    return head
