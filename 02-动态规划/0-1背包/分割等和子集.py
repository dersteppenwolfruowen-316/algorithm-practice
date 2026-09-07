class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 选/不选
        total = sum(nums)
        if total % 2 != 0:
            return False
        goal = total // 2
        @cache
        def dfs(i:int, target:int) -> bool:
            if i < 0:
                return target == 0 # bool
            if target < nums[i]:
                return dfs(i-1,target)
            return dfs(i-1, target - nums[i]) or dfs(i-1, target)
        
        return dfs(len(nums)-1, goal)