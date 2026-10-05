class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        #转化为0-1背包，且分为两堆：正号堆和负号堆
        #背包容量就是sum//2
        #容量target内能装入的最大值（石头的重量）
        total = sum(stones)
        target = sum(stones)//2
        dp = [0]*(target+1)
        for stone in stones:
            for i in range(target,stone-1,-1):
                dp[i] = max(dp[i], dp[i-stone]+stone) #dp[i]不选 dp[i-stone]+stone选

        return (total - 2*dp[target])