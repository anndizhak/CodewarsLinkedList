"""
Linked list node swapping module.
Provides functionality to swap adjacent pairs of nodes in-place.
"""
class Node(object):
    """
    Represents a single element (node) in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
def swap_pairs(head):
    """
    Swaps adjacent pairs of nodes in-place.
    Transforms 1->2->3->4 into 2->1->4->3 and returns the new head.
    """
    zero = Node(head)
    prev = zero
    first = head
    while first and first.next:
        second = first.next
        rest = second.next
        first.next = rest
        second.next = first
        prev.next = second
        prev = first
        first = rest
    return zero.next
