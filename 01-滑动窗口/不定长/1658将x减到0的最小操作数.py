class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 滑动窗口 = sum(nums) - x
        target = sum(nums) - x
        left = 0 
        ans = -1
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            while count > target and left <= i:
                count -= nums[left]
                left += 1
            if count == target:
                ans = max(ans, i - left + 1)
        return (len(nums) - ans ) if ans != -1 else -1

        