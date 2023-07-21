class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count = [] # this is where we will store the substring lenghts
        for i in range(len(s)):
            a, b = s[i], 1
            while True:
                try:
                    if s[i + b] not in a:
                        a += s[i + b]
                        b += 1
                    else:
                        count.append(len(a))
                except:
                    count.append(len(a))
        return max(count)


print(Solution().lengthOfLongestSubstring('abcabcbb'))