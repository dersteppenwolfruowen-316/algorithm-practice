class Solution:
    def minSwaps(self, data: List[int]) -> int:
        k = 0
        for i, c in enumerate(data):
            if c == 1:
                k += 1
        # 如果全是1或者没有1，不需要交换
        if k <= 1:
            return 0
        # 滑动窗口k中最少的0
        res = float("inf")
        nums = 0
        for i , c in enumerate(data):
            nums += c 
            left = i-k+1
            if left< 0:
                continue
            res = min(res, k - nums)
            nums -= data[left]
        return res



        