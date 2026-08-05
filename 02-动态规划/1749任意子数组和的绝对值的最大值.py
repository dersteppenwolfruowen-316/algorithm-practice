class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # 把最大子数组和最小子数组算出，再取绝对值最大
        ans = f_max = f_min = 0
        for x in nums:
            f_max = max(f_max, 0) + x
            f_min = min(f_min, 0) + x
            ans = max(ans, f_max, -f_min)
        return ans




        