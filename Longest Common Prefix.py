"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

"""
tests
strs = []
strs = ['a']
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        # create the return variable, and a count int variable
        # start an iteration, with a new variable that checks char at point of a string
        # if they are all the same, we add it to the return variable
        # if not the same, we return the return variable
        final_string, count = '', 0
        while True:
            a = set()
            if not strs:
                return final_string
            else:
                for item in strs:
                    if not item:
                        return final_string
                    else:
                        try:
                            a.add(item[count])
                        except:
                            return final_string
            if len(a) != 1:
                return final_string
            else:
                final_string += ''.join(list(a))
                count += 1


print(Solution().longestCommonPrefix(input().split())) # you can test with the test cases above


