"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#
# class Solution(object):
#     def reverseList(self, head):
#         a = []
#         if not head:
#             return head
#         else:
#             current = head
#             while current.next:
#                 a.append(current.val)
#                 current = current.next
#             a.append(current.val)
#             a = a[::-1]
#             x = None
#             for item in range(len(a)):
#                 if not x:
#                     x = ListNode(a[item])
#                 else:
#                     current = x
#                     while current.next:
#                         current = current.next
#                     current.next = ListNode(a[item])
#             return x

# OPTIMIZED SOLUTION O(n)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Optimized O(n) solution
        Create a return node which starts as None.
        Through each iteration through head:
            - the next of the current becomes current
            - the next of the current becomes a previously created variable prev which starts as None

        """
        if not head: return head
        last = None
        current = head
        while current:
            temp = current.next
            first = current
            first.next = last
            last = first
            current = temp
        return last