"""
You are given an array of words where each word consists of lowercase English letters.
wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the
order of the other characters to make it equal to wordB.
For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2,
word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.
Return the length of the longest possible word chain with words chosen from the given list of words.

Example 1:
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

Example 2:
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

Example 3:
Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
"""


def longestStrChain(self, words):
    dp = {}
    for w in sorted(words, key=len):
        dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
    return max(dp.values())


# class Solution:
#     def longestStrChain(self, words: [str]) -> int:
#         words.sort(key=lambda x: len(x))
#
#         def chain(first: str, second: str) -> bool:
#             final, index = '', 0
#             for i in range(len(second)):
#                 if not index < len(first):
#                     final += second[i:]
#                     break
#                 if second[i] == first[index]:
#                     final += second[i]
#                     index += 1
#                 else:
#                     final += second[i]
#
#             if len(final) - len(first) == 1 and index == len(first): return True
#             return False
#
#         count = 0
#         for i in range(len(words) - 1):
#             x = words[i]
#             my_list = [x, ]
#             for j in range(i + 1, len(words)):
#                 if chain(x, words[j]):
#                     my_list.append(words[j])
#                     x = words[j]
#
#             if len(my_list) > count: count = len(my_list)
#
#         return count





