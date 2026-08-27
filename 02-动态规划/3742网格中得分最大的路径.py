class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(i:int, j:int, cost:int) -> int:
            if i < 0 or j < 0:
                return -inf
            x = grid[i][j]
            need = 1 if x > 0 else 0
            if need > cost:
                return -inf
            if i == 0 and j == 0:
                return x
            return max(dfs(i-1, j, cost-need), dfs(i,j-1,cost-need)) + x
        ans = dfs(m - 1, n - 1, k)
        dfs.cache_clear() 
        return ans if ans != -inf else -1
        