"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?

[["0,0", "2,0", ]]
ABCCED
index = 1
current = "A"
while list:
    try: x = letters["A"][list[-1][-1]][index 1]
    except: list[-1].pop()
    else: list.append(letters[])
"""


class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        letters = {}
        for i in range(rows):
            for j in range(cols):
                try:
                    temp = letters[board[i][j]]
                except:
                    letters[board[i][j]] = {f"{i},{j}": {}}
                else:
                    temp[f"{i},{j}"] = {}

                if i == 0:
                    letters[board[i][j]][f"{i},{j}"][board[i + 1][j]] = f"{i + 1},{j}"
                    if j == 0:
                        letters[board[i][j]][f"{i},{j}"][board[i][j + 1]] = f"{i},{j + 1}"
                    elif j == cols - 1:
                        letters[board[i][j]][f"{i},{j}"][board[i][j - 1]] = f"{i},{j - 1}"
                    else:
                        letters[board[i][j]][f"{i},{j}"][board[i][j - 1]] = f"{i},{j - 1}"
                        letters[board[i][j]][f"{i},{j}"][board[i][j + 1]] = f"{i},{j + 1}"
                elif i == rows - 1:
                    letters[board[i][j]][f"{i},{j}"][board[i - 1][j]] = f"{i - 1},{j}"
                    if j == 0:
                        letters[board[i][j]][f"{i},{j}"][board[i][j + 1]] = f"{i},{j + 1}"
                    elif j == cols - 1:
                        letters[board[i][j]][f"{i},{j}"][board[i][j - 1]] = f"{i},{j - 1}"
                    else:
                        letters[board[i][j]][f"{i},{j}"][board[i][j - 1]] = f"{i},{j - 1}"
                        letters[board[i][j]][f"{i},{j}"][board[i][j + 1]] = f"{i},{j + 1}"
                else:
                    letters[board[i][j]][f"{i},{j}"][board[i + 1][j]] = f"{i + 1},{j}"
                    letters[board[i][j]][f"{i},{j}"][board[i - 1][j]] = f"{i - 1},{j}"
                    if j == 0:
                        letters[board[i][j]][f"{i},{j}"][board[i][j + 1]] = f"{i},{j + 1}"
                    elif j == cols - 1:
                        letters[board[i][j]][f"{i},{j}"][board[i][j - 1]] = f"{i},{j - 1}"
                    else:
                        letters[board[i][j]][f"{i},{j}"][board[i][j - 1]] = f"{i},{j - 1}"
                        letters[board[i][j]][f"{i},{j}"][board[i][j + 1]] = f"{i},{j + 1}"

        print(*letters.items(), sep="\n")


Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")

