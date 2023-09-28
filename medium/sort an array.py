"""
Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest
space complexity possible.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the
positions of other numbers are changed (for example, 1 and 5).

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

Constraints:
1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""


class Solution:
    def sortArray(self, nums: [int]) -> [int]:
        # use counting sort
        # first create a counting sort list for values between min and max of nums
        mini, maxi = min(nums), max(nums)
        counting = [0] * (maxi - mini + 1)
        # [-1, 3, 1, 2]
        # [1, 0, 1, 0, 1]
        for item in nums: counting[item - mini] += 1
        c = []
        for i in range(len(counting)):
            if not counting[i]: pass
            else: c += [mini] * counting[i]
            mini += 1

        return c