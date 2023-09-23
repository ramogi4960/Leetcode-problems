"""
You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two
elements that sum to it.

For example, consider nums = [5,6,7]. In one operation, we can replace nums[1] with 2 and 4 and convert nums to[5,2,4,7]
Return the minimum number of operations to make an array that is sorted in non-decreasing order.

Input: nums = [3,9,3]
Output: 2
Explanation: Here are the steps to sort the array in non-decreasing order:
- From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
- From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes [3,3,3,3,3]
There are 2 steps to sort the array in non-decreasing order. Therefore, we return 2.

Input: nums = [1,2,3,4,5]
Output: 0
Explanation: The array is already in non-decreasing order. Therefore, we return 0.

Input: nums = [12, 9, 7, 6]
Output: 6
Explanation: [12, 9, 7, 6] count = 0
[12, 9, 3, 4, 6] count = 1
[12, 3, 6, 3, 4, 6] count = 2
[12, 3, 3, 3, 3, 4, 6] count = 3
[3, 9, 3, 3, 3, 3, 4, 6] count = 4
[3, 3, 6, 3, 3, 3, 3, 4, 6] count = 5
[3, 3, 3, 3, 3, 3, 3, 3, 4, 6] count = 6
"""


class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:
        if nums == sorted(nums): return 0
        count = 0
        i = len(nums) - 1
        while i > 0:
            if nums[i] >= nums[i - 1]:
                i -= 1
            else:
                temp = nums[i - 1]
                # c = None
                # for item in range(1, temp + 1):
                #     if abs(item - (temp - item)) == 0:
                #         c = 0
                #         break
                #     else:
                #         if c == None:
                #             c = abs(item - (temp - item))
                #         else:
                #             if abs(item - (temp - item)) <= c:
                #                 c = abs(item - (temp - item))
                nums[i - 1] = nums[i]
                nums.insert(i - 1, temp - nums[i])
                count += 1

        return count


print(Solution().minimumReplacement([19, 7, 2, 24, 11, 16, 1, 11, 23]))
