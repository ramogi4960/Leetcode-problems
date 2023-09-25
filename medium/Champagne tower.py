"""
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th
row.  Each glass holds one cup of champagne.
Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid
poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any
excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has
its excess champagne fall on the floor.)
For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured,
the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full
- there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half
 full, and the two outside glasses are a quarter full.
 Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is
 (both i and j are 0-indexed.)

 Example 1:
Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no
excess liquid so all the glasses under the top glass will remain empty.

Example 2:
Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup
of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and
each will get half cup of champange.

Example 3:
Input: poured = 100000009, query_row = 33, query_glass = 17
Output: 1.00000

Constraints:
0 <= poured <= 109
0 <= query_glass <= query_row < 100
"""


# class Solution:
#     def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
#         matrix = [[1], ]
#         if poured == 1:
#             try: x = matrix[query_row][query_glass]
#             except: return 0
#             else: return x
#
#         if poured == 2:
#             matrix.append([0.5, 0.5])
#             try: x = matrix[query_row][query_glass]
#             except: return 0
#             else: return x
#
#         if poured == 3:
#             matrix.append([1, 1])
#             try: x = matrix[query_row][query_glass]
#             except: return 0
#             else: return x
#
#         matrix = [[1], [1, 1]]
#         ends_list, middle, ends, list_length = 1, 1, 0.5, 3
#
#         for i in range(3, poured + 1):
#             if matrix[-1][1] == 1:
#                 matrix.append([0] * list_length)
#                 list_length += 1
#                 middle /= 2
#                 for i in range(1, len(matrix[-1]) - 1):
#                     matrix[-1][i] += middle
#
#             else:
#                 for i in range(1, len(matrix[-1]) - 1):
#                     matrix[-1][i] += middle
#
#             if matrix[ends_list][0] == 1:
#                 ends_list += 1
#                 ends /= 2
#                 matrix[ends_list][0] += ends
#                 matrix[ends_list][-1] += ends
#
#             else:
#                 matrix[ends_list][0] += ends
#                 matrix[ends_list][-1] += ends
#
#         return matrix[query_row][query_glass]

# The above method is too slow especially when poured is a great number


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 1: return 1
        if poured == 2:
            matrix = [[1], [0.5, 0.5]]
            return matrix[query_row][query_glass]
        if poured == 3:
            matrix = [[1], [1, 1]]
            return matrix[query_row][query_glass]

        ends, middle, ends_list, ends_add, middle_add, list_len, middle_list, ends_list_len = 1, 1, 1, 0.5, 1, 2, 1, 2
        for i in range(4, poured - 1):
            if middle == 1:
                middle = 0
                middle_add /= 2
                middle += middle_add
                list_len += 1
                middle_list += 1
            else:
                middle += middle_add

            if ends == 1:
                ends = 0
                ends_add /= 2
                ends += ends_add
                ends_list += 1
                ends_list_len += 1
            else:
                ends += ends_add

        if query_row < ends_list: return 1
        elif query_row == ends_list:
            if query_glass == 0 or query_glass == ends_list_len - 1: return ends
            else: return 1
        else:
            if query_row == middle_list:
                if query_glass == 0 or query_glass == list_len - 1: return 0
                else: return middle
            else:
                if query_glass == 0 or query_glass == query_row - 1: return 0
                else: return 1


print(Solution().champagneTower(100000009, 33, 17))

