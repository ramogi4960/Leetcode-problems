"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: [int]) -> int:
        """
        Create variables, start, end, length, count, l,
        start and end are sliding window indices, length is the subarray length, count is the sum of subarray, and l is len(nums)
        Start while loop so long as index < l
        Through each iteration, check if count >= target
        If so, check if length is None.
            if so, l = (end - start) + 1
            else, check if l > (end - start) + 1. If so, l = (end - start) + 1
            Start another iteration until start == end while doing the above checks
        else, increment end
        [
        """

        if sum(nums) < target: return 0
        start = end = 0
        l, count = None, nums[0]

        while start < len(nums):
            if l == 1: return l
            if count >= target:
                if not l or (end - start) + 1 < l: l = (end - start) + 1
                while start != end:
                    count -= nums[start]
                    start += 1
                    if count >= target:
                        if (end - start) + 1 < l: l = (end - start) + 1
                    else:
                        break
            else:
                end += 1
                count += nums[end]
                if nums[end] >= target: return 1
                if end == len(nums) - 1: break

        while start != end:
            if count < target:
                if not l:
                    return 0
                else:
                    return l
            else:
                if not l or (end - start) + 1 < l: l = (end - start) + 1
                count -= nums[start]
                start += 1

        if not l:
            return 0
        else:
            return l

