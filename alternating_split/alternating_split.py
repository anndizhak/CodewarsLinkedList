"""
Module for splitting a linked list into two alternating sub-lists.
Separates nodes into 'first' (odd-indexed) and 'second' (even-indexed) lists.
"""
class Node(object):
    """
    Represents a single element (node) in a linked list.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    """
    A wrapper class to store and return the state of two linked lists.
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    """
    Splits a list into two, alternating nodes between them.
    Example: 1->2->3->4 becomes [1->3] and [2->4].
    """
    if not head or not head.next:
        raise Exception('Empty list or list with only one node!')
    count = 0
    probe = head
    curr_first = Node(0)
    curr_second = Node(0)
    res_first = curr_first
    res_second = curr_second
    while probe:
        if count % 2 == 0:
            curr_first.next = probe
            curr_first = curr_first.next
        else:
            curr_second.next = probe
            curr_second = curr_second.next
        probe = probe.next
        count += 1
    curr_first.next = None
    curr_second.next = None
    return Context(res_first.next, res_second.next)
