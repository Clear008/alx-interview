#!/usr/bin/python3
"""
    This module contains the canUnlockAll function.
"""

def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened
        Arg:
            boxes: Is a list of lists.
    """
    n = len(boxes)
    unlocked = set([0])
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == n
