"""
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).



Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]


Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
"""


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> [int]:
        if not root: return []
        nodes = [root, ]
        largest = [root.val, ]

        while nodes:
            temp = []
            values = []
            for item in nodes:
                if item.left:
                    temp.append(item.left)
                    values.append(item.left.val)
                if item.right:
                    temp.append(item.right)
                    values.append(item.right.val)
            if not temp: break

            largest.append(max(values))
            nodes = list(temp)

        return largest