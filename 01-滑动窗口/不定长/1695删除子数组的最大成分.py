class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        score = 0
        ans = 0
        e_count = defaultdict(int)
        left = 0
        for i in range(len(nums)):
            e_count[nums[i]] += 1
            score += nums[i]
            while e_count[nums[i]] > 1:
                e_count[nums[left]] -= 1
                score -= nums[left]
                left += 1
            ans = max(ans, score)    
        return ans    