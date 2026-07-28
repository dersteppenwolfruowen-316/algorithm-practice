class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_cnt = Counter(nums)
        k = len(total_cnt)
        left = 0
        ans = 0
        cnt = defaultdict(int)
        for right, num in enumerate(nums):
            cnt[num] += 1
            while len(cnt) == k: 
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            ans += left
        return ans