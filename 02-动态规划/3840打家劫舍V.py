class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
    
        f = [0]*(len(nums)+1)
        f[1] = nums[0]
        n = len(nums)
        for i in range(1, n):
            if colors[i] != colors[i-1]:
                f[i+1] = f[i] +nums[i]
            else:
                f[i+1] = max(f[i-1] + nums[i], f[i])
        return f[n]
        