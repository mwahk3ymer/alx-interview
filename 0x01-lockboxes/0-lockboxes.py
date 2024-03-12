#!/usr/bin/python3
''' module for lockboxes
'''

def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
    - boxes (List[List[int]]): A list of lists representing the boxes and keys.

    Returns:
    - bool: True if all boxes can be opened, else False.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    opened_boxes = set()
    opened_boxes.add(0)  # The first box is unlocked initially

    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key not in opened_boxes and 0 <= key < len(boxes):
                opened_boxes.add(key)
                stack.append(key)

    return len(opened_boxes) == len(boxes)
