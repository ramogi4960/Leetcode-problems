"""
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        new_nums = list(filter(lambda x: x > 0, sorted(nums)))
        if not new_nums:
            return 1
        if new_nums[0] != 1:
            return 1
        else:
            for i in range(len(nums)):
                try:
                    if new_nums[i+1] == new_nums[i]:
                        pass
                    elif new_nums[i+1] != new_nums[i] + 1:
                        return new_nums[i] + 1
                    else:
                        pass
                except:
                    return new_nums[i] + 1
