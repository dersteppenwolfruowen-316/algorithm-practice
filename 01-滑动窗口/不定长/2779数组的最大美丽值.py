class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        #排序之后找出一个子序列最大和最小值的差<=2k
        nums.sort()
        ans = left = 0
        for i, x in enumerate(nums):
            while x - nums[left] > 2*k:
                left += 1
            ans = max(ans, i - left + 1)
        return ans


        