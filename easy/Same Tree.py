"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false


Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        if not p and q or not q and p: return False

        def checking(head: TreeNode) -> [int]:
            items = [head.val, ]
            nodes =[head, ]
            for node in nodes:
                if node.left:
                    items.append(node.left.val)
                    nodes.append(node.left)
                else:
                    items.append(None)
                if node.right:
                    items.append(node.right.val)
                    nodes.append(node.right)
                else:
                    items.append(None)

            return items

        return checking(p) == checking(q)