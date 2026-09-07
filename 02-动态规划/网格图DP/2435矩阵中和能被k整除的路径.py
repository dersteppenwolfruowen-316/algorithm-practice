class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 1_000_000_007
        # s:路径和模k为s的路径数
        @cache
        def dfs(i:int, j:int, s:int) -> int:
            if i < 0 or j < 0:
                return 0
            pre_s = (s - grid[i][j]) % k
            if i == 0 and j == 0:
                return 1 if pre_s == 0 else 0 # s == grid[i][j] % k
            return (dfs(i-1, j, pre_s) + dfs(i, j-1, pre_s)) % MOD
        
        ans = dfs(len(grid) - 1, len(grid[0]) - 1, 0)
        dfs.cache_clear()
        return ans
            

