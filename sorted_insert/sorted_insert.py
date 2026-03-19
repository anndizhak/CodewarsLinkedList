"""
Module for inserting data into a sorted linked list.
"""
class Node(object):
    """
    Represents a single element (node) in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
def sorted_insert(head, data):
    """
    Inserts a value into the correct position in an ascending sorted linked list.
    """
    needed = Node(data)
    if not head or data < head.data:
        needed.next = head
        return needed
    prev = head
    curr = head.next
    while curr:
        if curr.data > data:
            break
        prev = curr
        curr = curr.next
    prev.next = needed
    needed.next = curr
    return head