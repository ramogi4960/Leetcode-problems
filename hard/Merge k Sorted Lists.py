"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Input: lists = []
Output: []

Input: lists = [[]]
Output: []
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return
        a = []
        for item in lists:
            if not item:
                pass
            else:
                current = item
                while current.next:
                    a.append(current.val)
                    current = current.next
                a.append(current.val)
        a.sort()
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