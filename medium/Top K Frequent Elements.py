"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in
any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        """
        create a set out of the [int]
        create a dict and add key value pairs by iterating through the set, adding the set items as keys and their count
        as their respective values
        sort the dict according the dict values
        return a list of the first k values
        """
        my_dict = dict()
        for item in set(nums):
            my_dict[item] = nums.count(item)

        return sorted(list(my_dict.keys()), key=lambda x: my_dict[x])[-k:]