class Solution:
    def rob(self, nums: List[int]) -> int:
        # 用两个元素维护优化空间
        prev = 0
        curr = 0
        for i in nums:
            # i 所在的元素下标是k
            # curr :dp[k-1] prev:dp[k-2]
            prev, curr = curr, max(curr, prev + i)    
        return curr    
        