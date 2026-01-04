"""
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.
If there is no such integer in the array, return 0.



Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
Example 2:

Input: nums = [21,21]
Output: 64
Example 3:

Input: nums = [1,2,3,4,5]
Output: 0


Constraints:

1 <= nums.length <= 104
1 <= nums[i] <= 105
"""

from math import sqrt, floor


class Solution:
    def sumFourDivisors(self, nums: [int]) -> int:
        final = 0
        for number in nums:
            # create store for divisors
            divisor = set()
            # find all divisors of number
            for i in range(1, floor(sqrt(number)) + 1):
                if number % i == 0:
                    divisor.add(number // i)
                    divisor.add(i)
                if len(divisor) > 4: break

            if len(divisor) == 4:
                final += sum(divisor)
        return final
