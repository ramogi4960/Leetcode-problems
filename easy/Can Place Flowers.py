"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: [int], n: int) -> bool:
        if n == 0: return True
        length = len(flowerbed)
        if length == 1:
            if flowerbed[0] == 0: return n == 1
        if length == 2:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                return n == 1
            else:
                return False
        index = 0

        while index < length:
            if flowerbed[index] == 0:
                if index == 0:
                    if flowerbed[index + 1] == 0:
                        flowerbed[index] = 1
                        n -= 1
                        index += 2
                    else:
                        index += 3
                elif index == length - 1:
                    if flowerbed[index - 1] == 0:
                        flowerbed[index - 1] = 1
                        n -= 1
                    index += 1
                else:
                    if flowerbed[index - 1] == 0 and flowerbed[index + 1] == 0:
                        flowerbed[index] = 1
                        n -= 1
                        index += 2
                    elif flowerbed[index - 1] == 0:
                        index += 3
                    elif flowerbed[index + 1] == 0:
                        index += 2
                    else:
                        index += 3
            else:
                index += 2
            if not n: return True

        return not n