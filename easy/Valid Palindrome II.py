"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                if left == right - 1: return True
                else: break
            left += 1
            right -= 1
        
        left_string = s[left:right]
        right_string = s[left + 1: right + 1]
        l, r = 0, len(left_string) - 1
        while l < r:
            if left_string[l] != left_string[r]: break
            l += 1
            r -= 1
        if not l < r: return True
        l, r = 0, len(right_string) - 1
        while l < r:
            if right_string[l] != right_string[r]: return False
            l += 1
            r -= 1
        return True