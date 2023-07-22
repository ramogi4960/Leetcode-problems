"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying
the values in the list's nodes (i.e., only nodes themselves may be changed.)

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Input: head = []
Output: []

Input: head = [1]
Output: [1]
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        a = []
        if not head or not head.next:
            return head
        else:
            current = head
            while current.next:
                a.append(current.val)
                current = current.next
            a.append(current.val)
        for i in range(0, len(a), 2):
            try:
                x = a[i + 1]
                a[i + 1] = a[i]
                a[i] = x
            except:
                pass
        head = None
        for item in a:
            if not head:
                head = ListNode(item)
            else:
                current = head
                while current.next:
                    current = current.next
                current.next = ListNode(item)
        return head
