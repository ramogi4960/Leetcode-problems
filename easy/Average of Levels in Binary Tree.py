"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.


Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> [float]:
        nodes = [root, ]
        averages = [root.val, ]
        while nodes:
            temp = []
            count = 0
            temp_sum = 0
            for node in nodes:
                if node.left:
                    temp.append(node.left)
                    count += 1
                    temp_sum += node.left.val
                if node.right:
                    temp.append(node.right)
                    count += 1
                    temp_sum += node.right.val
            nodes = temp
            if count: averages.append(round(temp_sum / count, 5))
        return averages