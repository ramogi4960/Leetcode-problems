"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.



Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2


Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        """
        Create variables for recording the level sum and the level
        start with level = 1 and sum = root.val
        Traverse through the tree breadth first
        If the sum of the current level > sum, update the values of sum and level
        Return level
        """
        max_sum = float("-inf")
        level = current_level = 0
        nodes = [root, ]
        while nodes:
            temp = []
            current_sum = 0
            current_level += 1
            for node in nodes:
                current_sum += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if current_sum > max_sum:
                max_sum = current_sum
                level = current_level
            nodes = temp
        return level