"""
Module for handling singly linked list structures and visualizations.
"""
class Node:
    """
    Represents a single element (node) in a linked list.
    """
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def stringify(node):
    """
    Converts a linked list of Nodes into a human-readable string representation.
    """
    result = ''
    while node is not None:
        result += f'{node.data} - > '
        node = node.next
    result += 'None'
    return result