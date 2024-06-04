#!/usr/bin/python3
'Lockboxes module'


def canUnlockAll(boxes):
    'Lockboxes'
    keys = []
    for box in boxes:
        if box == []:
            idx = boxes.index(box)
            if idx in keys:
                keys.append(idx + 1)
        for i in range(len(box)):
            if i == 0 or i in keys and box[i] != boxes.index(box):
                if box[i] not in keys and box[i] != 0:
                    keys.append(box[i])
        print(keys)
    if len(keys) == len(boxes) or len(keys) == len(boxes) - 1:
        return True
    return False
