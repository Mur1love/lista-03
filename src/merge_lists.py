from src.my_node import MyNode


def merge_lists(lista1: MyNode, lista2: MyNode) -> MyNode:
    dummy = MyNode(0)
    curr = dummy
    while lista1 is not None and lista2 is not None:
        if lista1.value <= lista2.value:
            curr.next = lista1
            lista1 = lista1.next
        else:
            curr.next = lista2
            lista2 = lista2.next
        curr = curr.next
    if lista1 is not None:
        curr.next = lista1
    if lista2 is not None:
        curr.next = lista2
    return dummy.next
