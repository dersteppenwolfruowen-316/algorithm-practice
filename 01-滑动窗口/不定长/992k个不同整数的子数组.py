class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        left1 = left2 = 0
        ch_count1 = defaultdict(int)
        ch_count2 = defaultdict(int)
        ans = 0
        for right, num in enumerate(nums):
            ch_count1[num] += 1
            ch_count2[num] += 1
            while len(ch_count1) >= k and left1 <= right:
                ch_count1[nums[left1]] -= 1
                if ch_count1[nums[left1]] == 0:
                    del ch_count1[nums[left1]]
                left1 += 1
            while len(ch_count2) >= k+1 and left2 <= right:
                ch_count2[nums[left2]] -= 1
                if ch_count2[nums[left2]] == 0:
                    del ch_count2[nums[left2]]
                left2 += 1
            ans += left1 - left2
        return ans 



        