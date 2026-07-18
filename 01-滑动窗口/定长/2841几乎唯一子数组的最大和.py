class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        same_el = defaultdict(int)
        sums = 0
        res = 0
        for right, num in enumerate(nums):
            sums += num
            same_el[num] += 1 #哈希表维护     
            left = right - k + 1
            if left < 0:
                continue
            # 加入m个唯一逻辑
            if len(same_el) >= m :
                res = max(res,sums)
            sums -= nums[left]
            same_el[nums[left]] -= 1
            if same_el[nums[left]] == 0:
                del same_el[nums[left]]
        return res
            
            
        