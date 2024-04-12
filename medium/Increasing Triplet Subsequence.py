"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.



Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.


Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1


Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""


class Solution:
    def increasingTriplet(self, nums: [int]) -> bool:
        stack = []
        seconds = None
        for item in nums:
            if not stack: stack.append(item)
            elif len(stack) == 1:
                if seconds is None:
                    if stack[-1] < item:
                        stack.append(item)
                    else:
                        stack = [item, ]
                else:
                    if item > seconds: return True
                    if stack[-1] < item:
                        stack.append(item)
                    else:
                        stack = [item, ]
            else:
                if item > stack[-1]: return True
                elif item == stack[-1]: pass
                else:
                    if item > stack[0]:
                        stack[-1] = item
                    else:
                        # seconds.append(stack[-1])
                        if seconds is None:
                            seconds = stack[-1]
                        else:
                            if stack[-1] < seconds: seconds = stack[-1]
                        stack = [item, ]
        return False