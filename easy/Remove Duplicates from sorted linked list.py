"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return head
        else:
            a = [head.val, ]
            current = head
            while current.next:
                if current.next.val not in a:
                    a.append(current.next.val)
                    current = current.next
                else:
                    current.next = current.next.next

            return head