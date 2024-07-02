#!/usr/bin/python3
"""canUnlockAll function."""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened """

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
