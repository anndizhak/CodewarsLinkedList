"""
Module for manual construction and manipulation of singly linked lists.
"""
class Node:
    """
    Represents a single element (node) in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
def push(head, data):
    """
    Creates a new Node with the given data and prepends it to the existing list.
    """
    first = Node(data)
    first.next = head
    return first
def build_one_two_three():
    """
    Builds a linked list with three nodes in the sequence: 1 -> 2 -> 3 -> None.
    """
    chained = None
    chained = push(chained, 3)
    chained = push(chained, 2)
    chained = push(chained, 1)
    return chained