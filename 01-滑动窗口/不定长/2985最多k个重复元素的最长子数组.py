class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ch_count = defaultdict(int)
        left = 0
        ans = 0
        for i in range(len(nums)):
            ch_count[nums[i]] += 1
            while ch_count[nums[i]] > k:
                ch_count[nums[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans

        