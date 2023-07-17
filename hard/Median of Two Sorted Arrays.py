"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        final = nums1 + nums2
        final.sort()
        x = len(final) // 2
        if len(final) % 2 == 0:
            f = final[x] + final[x - 1]
            return round(f/2, 5)
        else:
            return round(final[x], 5)


nums1, nums2 = [1, 2], [3, 4]
x = Solution()
print(x.findMedianSortedArrays(nums1, nums2))