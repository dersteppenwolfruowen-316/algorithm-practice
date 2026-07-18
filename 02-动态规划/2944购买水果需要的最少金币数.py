class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        # 从左往右
        n = len(prices)
        @cache
        def dfs(i:int) -> int:
            if i*2 >= n:
                return prices[i-1] 
            # dfs(i) = prices[i] + mindfs(j)
            # i+1<j<2i+1
            # i从1开始
            return min(dfs(j) for j in range(i+1,i*2+2)) + prices[i-1]
        return dfs(1)