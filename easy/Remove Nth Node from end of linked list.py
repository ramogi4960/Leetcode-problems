"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # we can do this by first creating a list of node values
        # then we remove hte nth value from the end
        # finally, we create a new linked list without the removed item
        a = []
        if not head:
            return head
        else:
            current = head
            while current.next:
                a.append(current.val)
                current = current.next
            a.append(current.val)
        # now a contains node values. So now we can remove the nth item from the end
        del a[-n]
        root = None
        for item in a:
            if not root:
                root = ListNode(item)
            else:
                current = root
                while current.next:
                    current = current.next