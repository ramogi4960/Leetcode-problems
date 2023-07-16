# Definition for singly-linked list.

"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Input: head = [1,1,1,2,3]
Output: [2,3]
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return head
        a, b = [], []
        current = head
        while current.next:
            a.append(current.val)
            current = current.next
        a.append(current.val)
        for item in a:
            if a.count(item) != 1:
                pass
            else:
                b.append(item)
        root = None
        for item in b:
            if not root:
                root = ListNode(item)
            else:
                current = root
                while current.next:
                    current = current.next
                current.next = ListNode(item)
        return root