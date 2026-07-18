class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sums = 0 
        res = float("inf")
        k_ = len(cardPoints) - k
        if k_ == 0:
            return sum(cardPoints) #直接return
        for right, p in enumerate(cardPoints):
            sums += p 
            left = right - k_ + 1
            if left < 0:
                continue
            res = min(res, sums)
            sums -= cardPoints[left]
        return sum(cardPoints) - res
        