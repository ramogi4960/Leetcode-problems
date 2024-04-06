"""
On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.



We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.



Example 1:

Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
Example 2:

Input: target = "code"
Output: "RR!DDRR!UUL!R!"


Constraints:

1 <= target.length <= 100
target consists only of English lowercase letters.
"""


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        letters = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                letters[board[i][j]] = [i, j]

        output = ""
        current = [0, 0]
        for item in target:
            position = letters[item]
            if item == "z":
                if current[0] < 5:
                    output += "D" * (4 - current[0])
                    if current[1] == 0: output += "D"
                    else: output += "L" * (current[1]) + "D"

            elif position[0] > current[0]:
                output += "D" * (position[0] - current[0])
                if position[1] > current[1]: output += "R" * (position[1] - current[1])
                elif position[1] < current[1]: output += "L" * (current[1] - position[1])
            elif position[0] < current[0]:
                output += "U" * (current[0] - position[0])
                if position[1] > current[1]: output += "R" * (position[1] - current[1])
                elif position[1] < current[1]: output += "L" * (current[1] - position[1])
            else:
                if position[1] > current[1]: output += "R" * (position[1] - current[1])
                elif position[1] < current[1]: output += "L" * (current[1] - position[1])
            output += "!"
            current = position
        return output