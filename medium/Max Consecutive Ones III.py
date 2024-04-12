"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""


class Solution:
    def longestOnes(self, nums: [int], k: int) -> int:
        longest = 0
        current = 0
        temp = k
        left = right = 0
        while right < len(nums):
            if temp:
                current += 1
                if nums[right] == 0: temp -= 1
            else:
                if nums[right] == 1: current += 1
                else:
                    while nums[left] == 1:
                        left += 1
                        current -= 1
                    left += 1
            right += 1
            if current > longest: longest = current
        return longest