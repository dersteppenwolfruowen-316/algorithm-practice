class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left = 0 
        ans = 0
        pair = 0
        ch_count = defaultdict(int)
        for right, num in enumerate(nums):
            pair += ch_count[num] 
            ch_count[num] += 1
            while pair >= k :  # >=,至少k对
                out = nums[left]
                ch_count[out] -= 1
                pair -= ch_count[out]
                left += 1
            ans += left
        return ans
        