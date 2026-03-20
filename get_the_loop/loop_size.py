"""
Module to calculate the length of a cycle in a linked list.
"""
def loop_size(node):
    """
    Return the number of nodes in the list's loop using fast and slow pattern.
    """
    if not node:
        return 0
    fast = node
    slow = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            count = 1
            curr = slow.next
            while curr != slow:
                curr = curr.next
                count += 1
            return count
