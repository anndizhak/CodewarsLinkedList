"""
Module for reversing a linked list using recursion.
"""
class Node(object):
    """
    Represents a single element (node) in a linked list.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None
def reverse(head):
    """
    Reverses the list in-place and returns the new head node.
    """
    def switcher(prev, curr):
        if not curr:
            return prev
        next_node = curr.next
        curr.next = prev
        return switcher(curr, next_node)
    return switcher(head, None)