class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        #子问题走到（i，j)位置满足XOR值条件的路径数
        # 多一个参数
        MOD = 1_000_000_007
        @cache
        def dfs(i:int, j:int, x:int) -> int:
            if i < 0 or j < 0:
                return 0
            val = grid[i][j]
            if i == 0 and j == 0:
                return 1 if x == val else 0
            return (dfs(i-1,j, x ^ val) + dfs(i,j-1, x ^ val)) % MOD
        ans = dfs(len(grid)-1, len(grid[0]) - 1, k)
        dfs.cache_clear()
        return ans