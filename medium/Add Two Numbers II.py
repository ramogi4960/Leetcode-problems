"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Input: l1 = [0], l2 = [0]
Output: [0]
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        first_list, a = [], l1
        while a.next:
            first_list.append(str(a.val))
            a = a.next
        first_list.append(str(a.val))

        second_list, b = [], l2
        while b.next:
            second_list.append(str(b.val))
            b = b.next
        second_list.append(str(b.val))

        while first_list[0] == '0' and len(first_list) != 1:
            del first_list[0]
        while second_list[0] == '0' and len(second_list) != 1:
            del second_list[0]


        final_number = int(''.join(first_list)) + int(''.join(second_list))
        root = None
        for item in list(str(final_number)):
            if not root:
                root = ListNode(int(item))
            else:
                current = root
                while current.next:
                    current = current.next
                current.next = ListNode(int(item))
        return root