class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = sum(nums) 
        if k == 0 :
            return 0
        n = len(nums)
        ones = 0
        max1 = 0
        for i in range(n+k-1):
            # 大于n的下标取模，映射到闭区间[0,n-1]中
            # 环形取模
            ones += nums[i % n]
            if i < k-1:
                continue
            max1 = max(max1,ones)

            ones -= nums[i-k+1] # i<n+k-1 -> i-k+1 < n,无需取模
        
        return k-max1 #最大的1，就可以最少的0，意味着交换次数最少
            
        