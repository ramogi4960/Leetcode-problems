class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


items = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = None
for i in range(len(items)):
    if i == 0:
        root = Node(items[i])
    elif i % 2 != 0:
        a = root.left
        while a:
            a = a.left
        a = Node(items[i])
        