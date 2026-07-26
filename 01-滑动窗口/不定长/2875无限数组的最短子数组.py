class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # 先计算total
        total = sum(nums)
        ans = float('inf')
        rem = target % total
        count = 0
        left = 0
        for i in range(2*n):
            count += nums[i % n]
            while count > rem :
                count -= nums[left % n]
                left += 1
            if count == rem:
                ans = min(ans, i - left + 1)
        return ans + target // total*n if ans < inf else -1