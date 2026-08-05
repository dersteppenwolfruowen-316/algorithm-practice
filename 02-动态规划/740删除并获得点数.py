class Solution:
    #相邻数字不能都选，就类似198
    # 把nums转换为一个值域数组，a[i]表示nums中等于i的元素之和
    def rob(self, nums: List[int]) -> int:
        f0 = f1 = 0
        for x in nums:
            f0, f1 = f1, max(f1, f0 + x)
        return f1
    
    def deleteAndEarn(self, nums: List[int]) -> int:
        a = [0] * (max(nums)+ 1) # 转为值域数组
        for x in nums:
            a[x] += x # 这样子就非常巧妙转化为了相邻数字
        return self.rob(a)


