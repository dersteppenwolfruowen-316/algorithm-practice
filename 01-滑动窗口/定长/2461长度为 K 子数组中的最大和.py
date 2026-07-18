class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        same_el = defaultdict(int)
        res = 0
        sums = 0
        for right, num in enumerate(nums):
            sums += num
            left = right - k + 1
            same_el[num] += 1
            if left < 0:
                continue
            if len(same_el) == k:
                res = max(res, sums)
            out = nums[left]
            sums -= out
            same_el[out] -= 1
            if same_el[out] == 0:
                del same_el[out]
        return res
        