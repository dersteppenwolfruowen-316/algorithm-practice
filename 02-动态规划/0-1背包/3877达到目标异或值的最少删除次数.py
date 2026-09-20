class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        # 目标是选的元素个数最多
        m = max(nums).bit_length()
        if (1 << m) <= target:
            return -1
        
        n = len(nums)
        f = [[-inf] * (1 << m) for _ in range(n + 1)]
        f[0][0] = 0

        for i, x in enumerate(nums):
            for j in range(1 << m):
                f[i + 1][j] = max(f[i][j], f[i][j ^ x] + 1)
        
        if f[n][target] < 0:
            return -1
        return n - f[n][target]
        