class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # 恰好型

        left1 = 0
        left2 = 0
        sums1 = sums2 =  0
        ans = 0
        for right, num in enumerate(nums):
            sums1 += num 
            sums2 += num
            while sums1 >= goal and left1 <= right:
                sums1 -= nums[left1]
                left1 += 1
            while sums2 >= goal + 1 and left2 <= right:
                sums2 -= nums[left2]
                left2 += 1
            ans += left1 - left2
        return ans