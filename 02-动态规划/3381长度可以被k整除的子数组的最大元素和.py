class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        #前缀和思路
        # max(prefix[j] - prefix[i])
        # j-i是长度
        pre = list(accumulate(nums, initial=0))
        min_s = [inf] * k
        ans = -inf
        for j,s in enumerate(pre):
            i = j % k
            ans = max(ans, s - min_s[i]) #维护关于模k同余的最小值就可
            min_s[i] = min(min_s[i], s) # 下一个长度为k的i，因为i = j % k
        return ans            
        