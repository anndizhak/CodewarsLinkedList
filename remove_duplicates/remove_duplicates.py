"""
Module for removing duplicate nodes from a sorted linked list.
Provides the remove_duplicates function to ensure unique node values.
"""
class Node(object):
    """
    Represents a single element (node) in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
def remove_duplicates(head):
    """
    Removes duplicates in a linked list.
    """
    if not head or not head.next:
        return head
    curr = head
    while curr is not None and curr.next is not None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head