"""
You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.



Example 1:


Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.
Example 2:


Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998.


Constraints:

The number of nodes in the list is in the range [1, 104]
0 <= Node.val <= 9
The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: ListNode) -> ListNode:
        x = head.val * 2
        if head.val > 4:
            final = ListNode(x // 10)
            final.next = ListNode(x - 10)
            final_current = final.next
        else:
            final = ListNode(x)
            final_current = final

        current = head
        while current.next:
            if current.next.val > 4:
                final_current.val += 1
                final_current.next = ListNode(current.next.val * 2 - 10)
            else:
                final_current.next = ListNode(current.next.val * 2)
            final_current = final_current.next
            current = current.next
        return final