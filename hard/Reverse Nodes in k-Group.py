"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a
multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""


# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        a = []
        if not head:
            return head
        else:
            current = head
            while current.next:
                a.append(current.val)
                current = current.next
            a.append(current.val)

        for i in range(0, len(a), k):
            if len(a[i:i + k]) == k:
                a[i:i + k] = a[i:i + k][::-1]
            else:
                pass

        root = None
        for item in a:
            if not root:
                root = ListNode(item)
            else:
                current = root
                while current.next:
                    current = current.next
                current.next = ListNode(item)
        return root