"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest
to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        my_dict = dict()
        for i in range(len(nums) - 2):
            count = 0
            j, k = i + 1, len(nums) - 1
            while j < k:
                p = nums[i] + nums[j] + nums[k]
                if p > target:
                    k -= 1
                    my_dict[abs(target - p)] = p
                elif p < target:
                    j += 1
                    my_dict[abs(target - p)] = p
                else:
                    j += 1
                    k -= 1
                    my_dict[0] = p

        return my_dict[min(list(my_dict.keys()))]