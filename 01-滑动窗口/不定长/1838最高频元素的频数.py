class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # 排序后只需找每个窗口里的数都变为最右边的数
        nums.sort()
        ans = 0
        left = 0
        count = 0
        for right,x in enumerate(nums):
            count += x
            # 只需计算差值
            while (right-left+1) * x - count > k :
                count -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans