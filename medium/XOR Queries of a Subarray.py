"""
You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

Return an array answer where answer[i] is the answer to the ith query.



Example 1:

Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8]
Explanation:
The binary representation of the elements in the array are:
1 = 0001
3 = 0011
4 = 0100
8 = 1000
The XOR values for queries are:
[0,1] = 1 xor 3 = 2
[1,2] = 3 xor 4 = 7
[0,3] = 1 xor 3 xor 4 xor 8 = 14
[3,3] = 8
Example 2:

Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
Output: [8,0,4,4]


Constraints:

1 <= arr.length, queries.length <= 3 * 104
1 <= arr[i] <= 109
queries[i].length == 2
0 <= lefti <= righti < arr.length
"""


class Solution:
    def xorQueries(self, arr: [int], queries: [[int]]) -> [int]:
        """
        create a new list where new_list[i] == XOR from arr[0] to arr[i] inclusive
        This shall be done by iterating through arr in linear time.
        Then, iterate through queries while recording values into a final return list.

        The final return list should be calculated using the following method:
        total ^ new_list[query[i][0] - 1] ^ total ^ new_list[query[i][1]]
        """

        # STEP 1: Create a new_list
        new_list = []
        # STEP 2: Fill the new list with XOR values from arr
        for item in arr:
            if not new_list:
                new_list.append(item)
            else:
                new_list.append(new_list[-1] ^ item)

        # STEP 3: Create a final list and add values into it using the formula:
        # new_list[-1] ^ new_list[query[i][0] - 1] ^ total ^ new_list[query[i][1]]
        final = []
        for item in queries:
            if item[0] == 0:
                final.append(new_list[item[1]])
            elif item[0] == item[1]:
                final.append(arr[item[0]])
            elif item[1] == len(arr) - 1:
                final.append(new_list[-1] ^ new_list[item[0] - 1])
            else:
                final.append( new_list[-1] ^ new_list[item[0] - 1] ^ new_list[-1] ^ new_list[item[1]])

        return final