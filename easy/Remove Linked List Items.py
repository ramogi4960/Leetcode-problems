"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val,
 and return the new head.

 Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Input: head = [], val = 1
Output: []

Input: head = [7,7,7,7], val = 7
Output: []
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return head
        else:
            current = head
            while current.next:
                if current.val == val and current == head:
                    head = current.next
                    current = head
                elif current.next.val == val:
                    current.next = current.next.next
                elif current.next.val != val:
                    current = current.next

            if head.val == val:
                head = head.next

            return head