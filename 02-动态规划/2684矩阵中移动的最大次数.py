class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # 因为是col+1向右移动，因此从第一列开始移动次数可以最大？
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int) -> int:
            # 返回：从 (i, j) 出发，还能再走多少步
            best = 0
            for ni in (i - 1, i, i + 1): # 用循环代替条件分支，因此正推更合适此题
                if 0 <= ni < m and j + 1 < n and grid[ni][j + 1] > grid[i][j]:
                    best = max(best, 1 + dfs(ni, j + 1))
            return best

        return max(dfs(i, 0) for i in range(m))