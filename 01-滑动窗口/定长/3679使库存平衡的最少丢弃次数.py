class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        kind = defaultdict(int)
        res = 0
        for i, c in enumerate(arrivals):
            if kind[c] == m: #当天等于m，丢弃
                arrivals[i] = 0 #丢弃arrivals[i]
                res += 1
            else:
                kind[c] += 1
            # 注意窗口<w的也成为窗口
            left  = i+1-w
            if left >= 0:
                kind[arrivals[left]] -= 1

        return res
            
        

        