"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        a = []
        if not list1:
            pass
        else:
            current = list1
            while current.next:
                a.append(current.val)
                current = current.next
            a.append(current.val)

        if not list2:
            pass
        else:
            current = list2
            while current.next:
                a.append(current.val)
                current = current.next
            a.append(current.val)

        a.sort()
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