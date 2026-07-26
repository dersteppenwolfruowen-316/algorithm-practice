class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        n = len(nums)
        s = 0 # 维护和就行，不用管外面窗口大小
        for right, num in enumerate(nums):
            s += num
            while s*(right-left+1) >= k:
                s -= nums[left]
                left += 1
            ans += right - left + 1
        return ans 





            
        