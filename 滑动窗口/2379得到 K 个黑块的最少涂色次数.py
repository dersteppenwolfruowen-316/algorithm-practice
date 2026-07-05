class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        b_sum = 0
        res = float("inf")
        right = 0 # 注意right位置
        for c in blocks:
            if c == "B":
                b_sum += 1
            left = right - k + 1
            if left < 0:
                right += 1
                continue
            res = min(res, (k-b_sum))
            if blocks[left] == "B":
                b_sum -=1   
            right += 1
        return res     