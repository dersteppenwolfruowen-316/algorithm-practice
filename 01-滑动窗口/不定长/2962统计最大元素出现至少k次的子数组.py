class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        left = 0
        freq = 0
        ans = 0
        for right, num in enumerate(nums):
            if num == max_num :
                freq += 1
            while freq == k:
                if nums[left] == max_num:
                    freq -= 1
                left += 1
            ans += left
        return ans 

        