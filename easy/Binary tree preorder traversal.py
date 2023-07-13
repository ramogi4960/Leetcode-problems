"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [1,2,3]

Input: root = []
Output: []

Input: root = [1]
Output: [1]

Input: root = [1,4,3,2]
Output: [1,4,2,3]
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

            
class Solution(object):
    def preorderTraversal(self, root):
        a = []
        if not root:
            return a
        else:
            x = [root, ]
            while x:
                y = []
                for item in x:
                    a.append(item.val)
                    if item.left:
                        y.append(item.left)
                    if item.right:
                        y.append(item.right)
                x = y

        return a



