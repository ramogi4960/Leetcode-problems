class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(n):
            if sum(list(range(1, i + 2))) == sum(list(range(i + 1, n + 1))): return i + 1
        return -1