class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划解法
        n = len(nums)
        # 子问题：以nums[i]为结尾的数组最大值
        @cache
        def dfs(i:int) -> int:
            if i == 0:
                return nums[0]
            else:
                return max(dfs(i-1),0) + nums[i]
        return max(dfs(i) for i in range(n))

        