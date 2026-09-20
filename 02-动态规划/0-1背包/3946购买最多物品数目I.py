
#0-1背包+枚举
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        f = [0] * (budget + 1)
        min_price = inf
        for factor, price in items:
            min_price = min(min_price, price)
            cnt = 0 #统计物品factor为此factor倍数的物品个数
            for factor_j, _ in items:
                if factor_j % factor == 0:
                    cnt += 1
            for j in range(budget, price-1, -1):
                f[j] = max(f[j], f[j-price] + cnt)
        return max(fi + (budget - i) // min_price for i, fi in enumerate(f))
            
        