class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        number_of_islands = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    c = j
                    while c < cols and grid[i][c] == "1":
                        grid[i][c] = "0"
                        r = i + 1
                        print(grid, end="\n")
                        while r < rows and grid[r][c] == "1":
                            grid[r][c] = "0"
                            left = c - 1
                            right = c + 1
                            while left > -1 and grid[r][left] == "1":
                                grid[r][left] = "0"
                                left -= 1
                            while right < cols and grid[r][right] == "1":
                                grid[r][right] = "0"
                                right += 1
                            r += 1
                        c += 1
                    number_of_islands += 1
        return number_of_islands


# Solution().numIslands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]])

print(*[["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]], sep="\n")