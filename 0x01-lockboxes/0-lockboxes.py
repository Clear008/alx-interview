#!/usr/bin/python3
"""canUnlockAll function."""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened """

    n = len(boxes)
    unlocked = set([0])
    visited = [0]

    while visited:
        current_box = visited.pop()
        for key in boxes[current_box]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                visited.append(key)

    return len(unlocked) == n
