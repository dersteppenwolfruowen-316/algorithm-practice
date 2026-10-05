class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        MOD = 10**9 + 7
        # dp定义盈利恰好profit时的子集个数
        # group <= n
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        for i in range(0, n + 1):
            dp[i][0] = 1
        for earn, members in zip(profit, group):
            for j in range(n, members - 1, -1):
                for k in range(minProfit, -1, -1):
                    dp[j][k] = (dp[j][k] + dp[j- members][max(0,k-earn)]) % MOD #不选这个工作和选这个工作
                    # max(0,k-earn) 把恰好为k转化为了至少为k,因为超出k也是允许的
        return dp[n][minProfit]



        