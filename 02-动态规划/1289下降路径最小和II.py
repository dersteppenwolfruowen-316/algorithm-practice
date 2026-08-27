class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        @cache
        def dfs(i:int, j:int) -> int:
            if i == 0:
                return grid[i][j]
            ans = inf
            for k in range(n):
                if k == j:
                    continue
                else:
                    ans = min(ans, dfs(i-1,k))
            return ans + grid[i][j]
        return min(dfs(n-1,k) for k in range(n))

        