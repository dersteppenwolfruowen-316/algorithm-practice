class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_count = defaultdict(int)
        left = 0
        ans = 0
        for i in range(len(nums)):
            num_count[nums[i]] += 1
            while num_count[0] > k:
                num_count[nums[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans          