class Solution:
    def maxSubArray(self, nums: List[int], repeat: int) -> int:
        ans = f = 0 
        for _ in range(repeat):
            for x in nums:
                f = max(f,0) + x
                ans = max(ans,f)
        return ans

    # 只有一直加正数，和才会更大
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if k == 1:
            return self.maxSubArray(arr, 1)
        ans = self.maxSubArray(arr, 2)
        ans += max(sum(arr),0)*(k-2)
        return ans % 1_000_000_007
        