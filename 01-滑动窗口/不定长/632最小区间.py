class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 先排序，再计算列表编号出现次数
        pairs = sorted((x, i) for (i, arr) in enumerate(nums) for x in arr)
        ans_l = -inf
        ans_r = inf
        empty = len(nums)
        cnt = [0] * empty
        left = 0
        for r, i in pairs:
            if cnt[i] == 0:
                empty -= 1
            cnt[i] += 1
            while empty == 0:
                l, i = pairs[left]
                if r - l < ans_r - ans_l:
                    ans_l, ans_r = l, r
                cnt[i] -= 1
                if cnt[i] == 0:
                    empty += 1
                left += 1
        return [ans_l, ans_r]
