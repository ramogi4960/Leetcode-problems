"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the
list from position left to position right, and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Input: head = [5], left = 1, right = 1
Output: [5]
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: [ListNode], left: int, right: int) -> [ListNode]:
        if not head or not head.next: return head
        linked_list, root = [head.val, ], head
        while root.next:
            linked_list.append(root.next.val)
            root = root.next

        middle_list = linked_list[left-1:right][::-1]
        left -= 1
        count = 0
        while left < right:
            linked_list[left] = middle_list[count]
            count += 1
            left += 1

        root = None
        for item in linked_list:
            if not root: root = ListNode(item)
            else:
                temp = root
                while temp.next: temp = temp.next
                temp.next = ListNode(item)

        return root
