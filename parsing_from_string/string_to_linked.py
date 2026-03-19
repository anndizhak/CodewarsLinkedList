"""
Module for parsing string representations of linked lists into Node objects.
"""
class Node:
    """
    Represents a single element (node) in a linked list.
    """
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def linked_list_from_string(list_repr: str) -> Node | None:
    """
    Constructs a linked list from a string formatted as '1 -> 2 -> None'.
    """
    parsed  = list_repr.split(' -> ')
    if not parsed:
        return None
    head =  Node(0)
    probe = head
    for i in parsed:
        if i in ['null', 'None']:
            break
        probe.next = Node(int(i))
        probe = probe.next
    return head.next
        


        