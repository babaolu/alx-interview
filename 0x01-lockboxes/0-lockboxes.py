#!/usr/bin/python3
"""
This module checks the possibility of opening boxes having key of one another
"""


def canUnlockAll(boxes):
    """ Checking if all boxes can be opened """
    if not boxes:
        return False
    locked = list(range(0, len(boxes)))
    return isUnlocked(boxes, 0, locked)


def isUnlocked(boxes, index, locked):
    """ Opening boxes for keys """
    if index in locked:
        locked.remove(index)
        if len(locked) == 0:
            return True
    else:
        return False

    for key in boxes[index]:
        free = isUnlocked(boxes, key, locked)
        if free is True:
            return free
    return False
