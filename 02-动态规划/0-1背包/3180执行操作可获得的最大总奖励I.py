class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        m = max(rewardValues)
        if m - 1 in rewardValues:
            return 2 * m - 1

        dp = [False] * (2 * m)      # dp[k]：总奖励 k 是否可达
        dp[0] = True
        for v in sorted(set(rewardValues)):
            for x in range(v):      # 只有 x < v 的状态才能选 v
                if dp[x]:
                    dp[x + v] = True

        for k in range(2 * m - 1, -1, -1):   # 从大到小找最大的可达状态
            if dp[k]:
                return k