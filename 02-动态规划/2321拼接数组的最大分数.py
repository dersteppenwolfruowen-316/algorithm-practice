class Solution:

    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        max_sum = f = 0
        ans = 0
        # dfs(i)定义为nums1[i]结尾的交换的最大值
        # 都为正数
        for x,y in zip(nums1, nums2):
            if f < 0: f = 0
            f += y-x
            if f > max_sum: max_sum = f
        ans = sum(nums1) + max_sum
        
        max_sum = f = 0
        for x,y in zip(nums2, nums1):
            if f < 0: f = 0
            f += y-x
            if f > max_sum: max_sum = f
        ans = max(ans, sum(nums2) + max_sum)

        return ans