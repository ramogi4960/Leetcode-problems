"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        Traverse through the binary tree breadth first. Through each iteration, add to a
        depth count
        Return the depth count after iteration ends
        """
        if not root: return 0
        if not root.left and not root.right: return 1
        depth = 0
        nodes = [root, ]
        while nodes:
            depth += 1
            temp = []
            for node in nodes:
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            nodes = temp
        return depth