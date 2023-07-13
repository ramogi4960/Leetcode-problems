class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return self.root
        else:
            current = [self.root, ]
            while current:
                a = []
                for item in current:
                    if not item.left:
                        item.left = Node(data)
                        return self.root
                    if not item.right:
                        item.right = Node(data)
                        return self.root
                    a.append(item.left)
                    a.append(item.right)
                current = a

    def printing(self):
        if not self.root:
            print('The binary tree is empty')
        else:
            current, temp = [self.root.data, ], [self.root, ]
            while temp:
                a = []
                for item in temp:
                    if item.left:
                        a.append(item.left)
                        current.append(item.left.data)
                    if item.right:
                        a.append(item.right)
                        current.append(item.right.data)
                temp = a

            print(*current, sep=', ')


x = BinaryTree()
root = None
for item in list(map(int, input().split())):
    root = x.insert(item)



