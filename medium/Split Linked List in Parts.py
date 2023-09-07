"""
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
The length of each part should be as equal as possible: no two parts should have a size differing by more than one.
This may lead to some parts being null.
The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size
greater than or equal to parts occurring later.
Return an array of the k parts.

Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size
than the later parts.

Constraints:

The number of nodes in the list is in the range [0, 1000].
0 <= Node.val <= 1000
1 <= k <= 50
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: [ListNode], k: int) -> [ListNode]:
        """
        Algorithm
        -> create a return list that will have all the parts of the linked list
        -> if k >= len(linked list), return a list of the linked list node, and None to fill extra spaces
        -> else, first find len(linked list) % k.
        -> the first len(linked list) % k items will have len(linked list)//k + 1
        -> the rest of the return list items will be linked lists of len(linked list)//k
        """
        if not head: return [None] * k

        """ create a list of all nodes of the linked list """
        linked_list, current = [head.val, ], head
        while current.next:
            linked_list.append(current.next.val)
            current = current.next

        """ if k > len(linked_list), return a list with the nodes of the linked list and None for extra spaces """
        if len(linked_list) <= k:
            final_list = [None] * k
            for i in range(len(linked_list)):
                final_list[i] = ListNode(linked_list[i])
            return final_list

        """ else, the first len(linked_list)%k items of the return list should have len(linked_list)//k + 1
            nodes and the rest should have len(linked_list)//k nodes
        """
        the_modulus, item_size, index = len(linked_list) % k, len(linked_list) // k, 0
        final_list = []
        # start linked list with item_size + 1 items and append to final_list
        # go through linked_list indexes
        # when modulus runs out, append final_list with linked lists of item_size items
        while index < len(linked_list):
            if the_modulus:
                root = None
                for item in linked_list[index:index + item_size + 1]:
                    if not root:
                        root = ListNode(item)
                    else:
                        temp = root
                        while temp.next: temp = temp.next
                        temp.next = ListNode(item)

                final_list.append(root)
                the_modulus -= 1
                index += item_size + 1

            else:
                root = None
                for item in linked_list[index:index + item_size]:
                    if not root:
                        root = ListNode(item)
                    else:
                        temp = root
                        while temp.next: temp = temp.next
                        temp.next = ListNode(item)

                final_list.append(root)
                index += item_size

        return final_list
