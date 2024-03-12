#!/usr/bin/python3

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

    # Initialize a set to keep track of opened boxes
    opened_boxes = set()
    opened_boxes.add(0)  # The first box is unlocked initially

    # Initialize a stack for DFS traversal
    stack = [0]

    while stack:
        current_box = stack.pop()

        # Check each key in the current box
        for key in boxes[current_box]:
            if key not in opened_boxes and 0 <= key < len(boxes):
                opened_boxes.add(key)
                stack.append(key)

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)


# Example Usage:
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Output: True

    boxes2 = [[1, 3], [3, 0, 1], [2], [0]]
    print(canUnlockAll(boxes2))  # Output: False
