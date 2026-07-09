class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        res = 0
        for i in range(n):
            res += prices[i] * strategy[i]
        change = 0

        # 计算初始窗口
        for j in range(k//2):
            change += (0-strategy[j]) * prices[j]
        for j in range(k//2, k):
            change += (1-strategy[j]) * prices[j]
        ans = max(res, res + change)
        # out肯定是变化为0 in 肯定是变化为1，中间也要从变为1 而变为0
        for start in range(1, n - k + 1):
            # 移除左边元素（它之前是变为0的部分）
            left = start - 1
            change -= (0 - strategy[left]) * prices[left]
            
            # 元素 start + half - 1 从"变为1"变成"变为0"
            mid = start + k//2 - 1
            change -= (1 - strategy[mid]) * prices[mid]
            change += (0 - strategy[mid]) * prices[mid]
            # 加入右边新元素（变为1）
            right = start + k - 1
            change += (1 - strategy[right]) * prices[right]
            ans = max(ans, res + change)
        return ans

        