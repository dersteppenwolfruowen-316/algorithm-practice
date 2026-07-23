class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        ch_count = defaultdict(int)
        max_freq = 0
        for right in range(len(nums)):
            ch_count[nums[right]] += 1
            max_freq = max(max_freq, ch_count[nums[right]])
            while (right - left + 1) - max_freq > k and left < right:
                ch_count[nums[left]] -= 1
                if ch_count[nums[left]] == 0:
                    del ch_count[nums[left]] 
                left += 1
            ans = max(ans, right- left + 1)
        return max_freq
        