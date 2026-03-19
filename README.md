# CodewarsLinkedList

This repository contains solutions to Linked List problems from the Codewars platform.

## Task Structure

### Simple
- Convert a linked list to a string
- Parse a linked list from a string
- Linked Lists - Push & BuildOneTwoThree
- Linked Lists - Get Nth Node
- Linked Lists - Move Node

### Middle
- Linked Lists - Sorted Insert
- Linked Lists - Recursive Reverse
- Linked Lists - Remove Duplicates

### Hard
- Swap Node Pairs In Linked List
- Linked Lists - Alternating Split
- Can you get the loop? (Implemented using the Fast and Slow pointers pattern)

---

## Key Concepts: Fast and Slow Pattern

The Fast and Slow pointers pattern (also known as Floyd's Cycle-Finding Algorithm) is an efficient approach for linked list traversal. It is primarily used for:

1. Detecting cycles in a linked list.
2. Finding the middle element of a list.
3. Identifying the starting point of a cycle.

The algorithm uses two pointers moving at different speeds (typically one step and two steps). This allows solving complex list problems with O(n) time complexity and O(1) space complexity.