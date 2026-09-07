class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:

        f = [0] + [-1] * target   # f[j] 表示凑出和为 j 的最长子序列长度，-1 表示不可达
        for x in nums:
            for j in range(target, x - 1, -1): 
                if f[j - x] != -1:
                    f[j] = max(f[j], f[j - x] + 1)
        return f[target]