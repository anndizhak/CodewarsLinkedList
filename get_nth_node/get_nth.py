"""
Module for retrieving specific nodes from a linked list by their index.
"""
class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def get_nth(node, index):
    """
    Returns the node at the specified index position in a linked list.
    """
    if node is None or index < 0:
        raise Exception('Empty list or unappropriate index')
    probe = node
    count = 0
    while probe:
        if count == index:
            return probe
        count+=1
        probe = probe.next
    raise Exception('Index out of range')