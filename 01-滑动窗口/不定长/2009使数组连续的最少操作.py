class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        ans = 0
        # 我原来的思路：排序后找出最长满足条件的子数组
        # 计数窗口内的重复整数
        # 更好的思路是先去重再找最长连续子数组
        unique_nums = sorted(set(nums))
        m = len(unique_nums)
        
        for right, num in enumerate(unique_nums):
            while num - unique_nums[left] >= n:
                left += 1
            ans = max(ans, right - left + 1)
        return n-ans
            

        