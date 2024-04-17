"""
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.



Example 1:


Input: root = [0,1,2,3,4,3,4]
Output: "dba"
Example 2:


Input: root = [25,1,3,1,3,0,2]
Output: "adz"
Example 3:


Input: root = [2,2,1,null,1,0,null,0]
Output: "abc"


Constraints:

The number of nodes in the tree is in the range [1, 8500].
0 <= Node.val <= 25
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        """
        Create a final list to store the list of strings from root to leaf
        Traverse through the tree
        """
        final = []
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        nodes = [root, ]
        words = [alphabet[root.val],]

        while nodes:
            temp = []
            temp_words = []
            for i in range(len(nodes)):
                if nodes[i].left:
                    temp.append(nodes[i].left)
                    temp_words.append(alphabet[nodes[i].left.val] + words[i])
                if nodes[i].right:
                    temp.append(nodes[i].right)
                    temp_words.append(alphabet[nodes[i].right.val] + words[i])
                if not nodes[i].left and not nodes[i].right:
                    final.append(words[i])
            nodes = temp
            words = temp_words
        return sorted(final)[0]
