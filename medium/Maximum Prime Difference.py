"""
You are given an integer array nums.

Return an integer that is the maximum distance between the indices of two (not necessarily different) prime numbers in nums.



Example 1:

Input: nums = [4,2,9,5,3]

Output: 3

Explanation: nums[1], nums[3], and nums[4] are prime. So the answer is |4 - 1| = 3.

Example 2:

Input: nums = [4,8,2,8]

Output: 0

Explanation: nums[2] is prime. Because there is just one prime number, the answer is |2 - 2| = 0.



Constraints:

1 <= nums.length <= 3 * 105
1 <= nums[i] <= 100
The input is generated such that the number of prime numbers in the nums is at least one.
"""


class Solution:
    def maximumPrimeDifference(self, nums: [int]) -> int:
        def prime(number: int) -> bool:
            if number == 1: return False
            if number in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]: return True
            for i in range(2, (number // 2) + 1):
                if number % i == 0: return False
            return True

        left = right = None
        for i in range(len(nums)):
            if prime(nums[i]):
                if left is None:
                    left = i
                else:
                    right = i
        return 0 if right is None else abs(left - right)
