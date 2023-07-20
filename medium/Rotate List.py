"""
Given the head of a linked list, rotate the list to the right by k places.

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        if not head or not k or not head.next:
            return head
        if not head.next.next:
            for i in range(k):
                x = head.next
                head.next = None
                y = head
                head = x
                x.next = y
            return head
        a = []
        current = head
        while current.next:
            a.append(current.val)
            current = current.next
        a.append(current.val)
        root = None
        if k > len(a):
            k = k % len(a)  # we do this so as not to exceed space and time limit
        elif k == len(a):
            return head

        for i in range(k):
            a.insert(0, a.pop())

        for item in a:
            if not root:
                root = ListNode(item)
            else:
                temp = root
                while temp.next:
                    temp = temp.next
                temp.next = ListNode(item)
        return root
