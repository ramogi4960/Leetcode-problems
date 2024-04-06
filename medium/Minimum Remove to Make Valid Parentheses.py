"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.


Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Initialize a count variable for recording number of brackets
        Itrarete through s while adding items to a return list
        If s[i] == '(', increment count
        If s[i] == ')' and count == 0, do not add it to the return string
        else, decrement count
        After the iteration ends, if count > 0, replace excess ')' with nothing and return
        the string
        Else, return the string as it is
        """
        count, final = 0, ""
        for item in s:
            if item == "(":
                count += 1
                final += item
            elif item == ")":
                if count:
                    count -= 1
                    final += item
            else:
                final += item

        return final[::-1].replace("(", "", count)[::-1]