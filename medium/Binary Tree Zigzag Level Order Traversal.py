"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> [[int]]:
        if not root: return []
        nodes = [root, ]
        final = [[root.val, ], ]
        truth = True
        while nodes:
            temp = []
            temp_values = []
            for node in nodes:
                if node.left:
                    temp.append(node.left)
                    temp_values.append(node.left.val)
                if node.right:
                    temp.append(node.right)
                    temp_values.append(node.right.val)
            nodes = temp
            if temp_values:
                if truth: final.append(temp_values[::-1])
                else: final.append(temp_values)
                truth = not truth
        return final