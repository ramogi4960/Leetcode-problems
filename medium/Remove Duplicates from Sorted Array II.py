"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique
element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed
in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the
first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra
memory.

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively
It does not matter what you leave beyond the returned k (hence they are underscores).

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3
respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""


class Solution(object):
    def removeDuplicates(self, nums):
        new_nums = []
        for item in nums:
            if new_nums.count(item) < 2:
                new_nums.append(item)
            else:
                pass

        count = 0
        for i in range(len(nums)):
            try:
                nums[i] = new_nums[i]
                count += 1
            except:
                nums[i] = '_'

        return count