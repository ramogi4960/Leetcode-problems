"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater
than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Input: head = [2,1], x = 2
Output: [1,2]
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def partition(self, head, x):
        a, b = [], []
        if not head:
            return head
        else:
            current = head
            while current.next:
                if current.val < x:
                    a.append(current.val)
                    current = current.next
                else:
                    b.append(current.val)
                    current = current.next
            if current.val < x:
                a.append(current.val)
            else:
                b.append(current.val)
        a, root = a + b, None
        for item in a:
            if not root:
                root = ListNode(item)
            else:
                current = root
                while current.next:
                    current = current.next
                current.next = ListNode(item)
        return root