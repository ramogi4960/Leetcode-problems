"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""


class Solution:
    def trap(self, height: [int]) -> int:
        first_item = height[0]
        index = 1
        while index < len(height):
            if height[index] >= first_item:
                first_item = height[index]
                index += 1
            else:
                stack = [first_item, ]
                break

        count = 0
        while index < len(height):
            if height[index] <= stack[-1]:
                stack.append(height[index])
            else:
                if height[index] >= stack[0]:
                    for item in stack[1:]: count += stack[0] - item
                    stack = [height[index], ]
                else:
                    k = -1
                    while stack[k] < height[index]:
                        count += height[index] - stack[k]
                        stack[k] = height[index]
                        k -= 1
                    stack.append(height[index])
            index += 1
        return count