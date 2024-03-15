"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        if len(set(nums)) == 1 and nums[0] == 0: return [0] * len(nums)
        from math import prod
        if 0 in nums:
            product = prod(list(filter(lambda x: x != 0, nums)))
            if nums.count(0) > 1:
                return [0] * len(nums)
            else:
                return [0 if item != 0 else product for item in nums]
        else:
            product = prod(nums)
            return [product // item for item in nums]

