#!/usr/bin/python3
""" check if all boxes in the list of list can be opened """


def canUnlockAll(boxes):
    """ determin if all boxes can be opened """
    for key in range(1, len(boxes) - 1):
        result = False
        for index in range(len(boxes)):
            result = key in boxes[index] and key != index
            if result:
                break
        if result is False:
            return result
    return True
