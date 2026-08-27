class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        # 把奇数秒+偶数秒一起看作一步
        # 子问题是到底（i，j）的最小总成本，而要到达（i,j），一定在（i-1，j)或（i,j-1）等待一秒
        @cache
        def dfs(i:int, j:int) -> int:
            if i < 0 or j < 0:
                return inf
            if i == 0 and j == 0:
                return 1
            return min(dfs(i, j - 1), dfs(i - 1, j)) + waitCost[i][j] + (i + 1) * (j + 1)
        return dfs(m-1, n-1) - waitCost[-1][-1] #终点不需要等待