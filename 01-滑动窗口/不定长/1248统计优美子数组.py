class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left1 = left2 = 0
        sums1 = sums2 = 0
        ans = 0
        for right, num in enumerate(nums):
            if num % 2 == 1:
                sums1 += 1
                sums2 += 1
            while sums1 >= k and left1 <= right:
                if nums[left1] % 2 == 1:
                    sums1 -= 1
                left1 += 1
            while sums2 >= k+1 and left2 <= right:
                if nums[left2] % 2 == 1:
                    sums2 -= 1
                left2 += 1
            ans += left1 - left2
        return ans

        