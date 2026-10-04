class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        # 把配料扩展两倍，这样就是0-1背包问题？
        # 数组dp记录小于等于target的可达状态
        # 最接近可以想象为距离，因此分为上方和下方
        x = min(baseCosts)
        if x >= target:          # 最便宜的基料都不低于 target，加东西只会更远
            return x

        dp = [False] * (target + 1)
        ans = 2 * target - x     # 一个足够大的初始上界（任何有效答案的差距不会比它更差）
        for b in baseCosts:
            if b <= target:
                dp[b] = True # 小于等于taget的进入dp
            else:
                ans = min(ans, b) # 大于target的用ans记录
        for t in toppingCosts * 2:           # 复制两份，转成 0-1 背包
            for j in range(target, 0, -1):   # 倒序，保证每件物品只用一次
                if dp[j] and j + t > target:
                    ans = min(ans, j + t)    # 超出 target 的第一步，记录即可
                if j - t > 0 and dp[j - t]:
                    dp[j] = True
        # 下方最近的可达价格
        for j in range(target, -1, -1):
            if dp[j]:
                lo = j
                break
        # 比较 lo 和 ans
        return lo if target - lo <= ans - target else ans # ans是超出target的


        