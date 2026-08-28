class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        # 因为负数的存在需要同时维护最大积和最小积
        @cache
        def dfs(i:int, j:int) -> int:
            val = grid[i][j]
            if i == 0 and j == 0:
                return (val, val)
            candidates = [] # 子问题所有候选加入

            if i > 0:
                candidates.append(dfs(i - 1, j))
            if j > 0:
                candidates.append(dfs(i, j - 1))

            prods = []
            for mx, mn in candidates:
                # mx*val和mn*val可能分别称为mn和mx
                prods.append(mx * val)
                prods.append(mn * val)

            return (max(prods), min(prods))

        mx, _ = dfs(m - 1, n - 1)
        return mx % MOD if mx >= 0 else -1
        