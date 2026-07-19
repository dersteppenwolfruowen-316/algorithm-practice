class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        #先排序
        nums.sort()
        ans = 0
        left = 0
        for i, num in enumerate(nums):
            # 计算当前窗口的最值要放在while里面
            while True:
                max_num = num
                min_num = nums[left]
                if max_num <= k * min_num:
                    break
                left += 1
            ans = max(ans, i - left + 1)
        return len(nums) - ans


        