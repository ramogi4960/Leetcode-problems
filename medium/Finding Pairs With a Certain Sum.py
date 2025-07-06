"""
You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of
two types:

Add a positive integer to an element of a given index in the array nums2.
Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value (0 <= i < nums1.length and
0 <= j < nums2.length).
Implement the FindSumPairs class:

FindSumPairs(int[] nums1, int[] nums2) Initializes the FindSumPairs object with two integer arrays nums1 and nums2.
void add(int index, int val) Adds val to nums2[index], i.e., apply nums2[index] += val.
int count(int tot) Returns the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.


Example 1:

Input
["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
Output
[null, 8, null, 2, 1, null, null, 11]

Explanation
FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
findSumPairs.count(7);  // return 8; pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5)
make 3 + 4
findSumPairs.add(3, 2); // now nums2 = [1,4,5,4,5,4]
findSumPairs.count(8);  // return 2; pairs (5,2), (5,4) make 3 + 5
findSumPairs.count(4);  // return 1; pair (5,0) makes 3 + 1
findSumPairs.add(0, 1); // now nums2 = [2,4,5,4,5,4]
findSumPairs.add(1, 1); // now nums2 = [2,5,5,4,5,4]
findSumPairs.count(7);  // return 11; pairs (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) make 2 + 5
and pairs (5,3), (5,5) make 3 + 4


Constraints:

1 <= nums1.length <= 1000
1 <= nums2.length <= 105
1 <= nums1[i] <= 109
1 <= nums2[i] <= 105
0 <= index < nums2.length
1 <= val <= 105
1 <= tot <= 109
At most 1000 calls are made to add and count each.
"""

class FindSumPairs:
    """
    Create a counter dict for nums2, with the number as the keys and their respective counts as values.
    For the .add(), decrement the number from the counter dict, update nums[index], then increment the new
    number in the counter dict.
    For the .count(), iterate through nums1, adding the count of counter_dict[tot - nums1[i]], then return that value.
    """

    def __init__(self, nums1: list[int], nums2: list[int]):
        # O(n + m) worst case == 10**8 steps
        self.nums1 = nums1
        self.nums2 = []
        self.nums2_dict = {} # represents the count of unique numbers in nums2
        for item in nums2:
            try:
                self.nums2_dict[item] += 1
            except:
                self.nums2_dict[item] = 1
            finally:
                self.nums2.append(item)

    def add(self, index: int, val: int) -> None:
        # O(3) worst case == 3 steps
        # decrement its count
        self.nums2_dict[self.nums2[index]] -= 1
        if self.nums2_dict[self.nums2[index]] == 0:
            del self.nums2_dict[self.nums2[index]]
        # update the value in self.nums2
        self.nums2[index] += val
        # increment the count of the new number
        try:
            self.nums2_dict[self.nums2[index]] += 1
        except:
            self.nums2_dict[self.nums2[index]] = 1

        return

    def count(self, tot: int) -> int:
        # O(n) worst case == len(self.nums1) steps
        total_count = 0
        for number in self.nums1:
            try:
                total_count += self.nums2_dict[tot - number]
            except:
                continue
        return total_count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)