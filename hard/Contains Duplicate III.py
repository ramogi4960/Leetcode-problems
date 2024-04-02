"""
You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.



Example 1:

Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
Example 2:

Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.


Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
1 <= indexDiff <= nums.length
0 <= valueDiff <= 109
"""


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: [int], indexDiff: int, valueDiff: int) -> bool:
        numbers = {}
        for i in range(len(nums)): numbers[i] = nums[i]
        numbers = [[item[1], item[0]] for item in sorted(numbers.items(), key=lambda x: x[1])]
        left = 0
        while left < len(numbers):
            right = left + 1
            while right < len(nums):
                if right > len(nums): break
                if abs(numbers[right][0] - numbers[left][0]) <= valueDiff:
                    if abs(numbers[right][1] - numbers[left][1]) <= indexDiff:
                        return True
                    else:
                        right += 1
                else:
                    break
            left += 1
        return False

