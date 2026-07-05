class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        avg = 0
        for right, num in enumerate(nums):
            avg += num
            left = right - 2*k
            mid = right - k
            if mid < 0 :
                continue
            if left < 0:
                continue
            res[mid] = avg // (k * 2 + 1)

            avg -= nums[left]
        
        return res


        