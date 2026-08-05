class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 类似于爬楼梯，一共有target楼梯需要爬
        # 而每一步都可以爬nums[i]个楼梯
        @cache
        def dfs(i:int) -> int:
            if i==0:
                return 1
            return sum(dfs(i-x) for x in nums if x<= i)
        return dfs(target)
        