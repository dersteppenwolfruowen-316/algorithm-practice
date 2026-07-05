class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        ans = [0]*((len(nums)-k)+1)
        same_el = defaultdict(int)
        for right, c in enumerate(nums):
            same_el[c] += 1
            left = right -k +1
            if left < 0:
                continue
            ans[left] = len(same_el)
            out = nums[left]
            same_el[out] -= 1
            if same_el[out] == 0:
                del same_el[out]
        return ans

        