class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        @cache
        def dfs(i:int, j:int, skip:int) -> int:
            if i < 0 or j < 0:
                return -inf
            x = coins[i][j]
            if i == 0 and j == 0:
                return max(x, 0) if skip else x
            res = max(dfs(i-1, j, skip), dfs(i, j-1, skip)) + x #选
            if skip and x < 0:
                res = max(res, dfs(i-1, j, skip-1), dfs(i, j-1, skip-1)) #不选，跳过
            return res
            
        ans = dfs(m-1,n-1,2)
        dfs.cache_clear() 
        return ans