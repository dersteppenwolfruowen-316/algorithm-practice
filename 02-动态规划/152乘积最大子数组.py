class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dfs(i)表示以nums[i]为结尾的最大乘积
        # 因为是整数数组大于1，因此不管符号的话乘的数越多一定越大
        # 因此同时维护nums[i-1]为结尾的最大值和最小值，再乘x,这样就无需考虑x的符号
        n = len(nums)
        f_max = [0]*n
        f_min = [0]*n 
        f_max[0] = f_min[0] = nums[0]
        for i in range(1, n):
            x = nums[i]
            f_max[i] = max(f_max[i-1]*x, f_min[i-1]*x, x)
            f_min[i] = min(f_max[i-1]*x, f_min[i-1]*x, x)
        return max(f_max) # max(dfs(i))是不需要返回dfs(n)的因为不一定是nums[n]结尾的最大

        