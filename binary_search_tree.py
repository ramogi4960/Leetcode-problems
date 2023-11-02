class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def insert(root: Node, value: int):
    if not root:
        root = Node(value)
        return root
    else:
        current = root
        while True:
            if value <= current.value:
                if not current.left:
                    current.left = Node(value)
                    break
                else:
                    current = current.left
            else:
                if not current.right:
                    current.right = Node(value)
                    break
                else:
                    current = current.right
        return root


def printing(head: Node):
    if not head:
        return f"The head is empty"
    else:
        items = [head.value, ]
        nodes = [head, ]
        for item in nodes:
            if item.left:
                items.append(item.left.value)
                nodes.append(item.left)
            if item.right:
                items.append(item.right.value)
                nodes.append(item.right)
        return items


my_list = [7, 4, 3, 12, 34, 1, 0, 5, 6, 9, 8]
root = None

for item in my_list:
    root = insert(root, item)


print(printing(root))