"""
Module for shifting nodes between linked lists using a Context object.
"""
class Node(object):
    """
    Represents a single element (node) in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
class Context(object):
    """
    A wrapper class to store and return the state of two linked lists.
    """
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
def move_node(source, dest):
    """
    Moves the front node from the source list to the front of the destination list.
    """
    if not source:
        raise Exception('List is empty')
    probe = source
    new_source = source.next
    probe.next = dest
    new_dest = probe
    return Context(new_source,new_dest)