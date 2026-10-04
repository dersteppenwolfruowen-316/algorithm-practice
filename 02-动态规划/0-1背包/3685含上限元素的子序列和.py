class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        nums.sort()
        n = len(nums)
        ans = [False] * n 
        f = [False] * (k+1)
        f[0] = True

        i = 0
        for x in range(1, n+1):
            # 巧妙：增量考虑所有恰好等于x的数字
            while i < n and nums[i] == x:
                for j in range(k, nums[i]-1, -1):
                    f[j] = f[j] or f[j-nums[i]] # 不选，选
                i += 1
            for j in range(min(n-i, k//x)+1):
                if f[k-j * x]:
                    ans[x-1] = True
                    break
        return ans