"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item in "([{":
                stack.append(item)
            else:
                if not stack: return False
                if stack[-1] == "(" and item == ")":
                    stack.pop()
                elif stack[-1] == "[" and item == "]":
                    stack.pop()
                elif stack[-1] == "{" and item == "}":
                    stack.pop()
                else:
                    return False

        return not stack


""" THE CODE IN JAVASCRIPT """

"""
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = [];
    let l = 0
    for (item of s) {
        if (("([{").indexOf(item) !== -1) {
            stack.push(item);
            l += 1;
        }
        else {
            if (stack[l - 1] === "(" && item === ")"  ) {
                stack.pop();
                l -= 1;
            }
            else if ( stack[l - 1] === "{" && item === "}"  ) {
                stack.pop();
                l -= 1;
            }
            else if ( stack[l - 1] === "[" && item === "]"  ) {
                stack.pop();
                l -= 1;
            }
            else { return false }
        }
    }
    return l === 0;
};
"""