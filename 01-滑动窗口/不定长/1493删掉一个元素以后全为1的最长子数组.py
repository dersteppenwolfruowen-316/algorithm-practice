class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 转换为只包含1或包含一个0的最长子串
        left = 0
        ans = 0
        sum_num = 0
        for right,i in enumerate(nums):
            sum_num += i
            while abs(sum_num - (right-left+1) ) > 1 and left < right:
                sum_num -= nums[left]
                left += 1
            ans = max(ans, right-left)
        return ans
        