class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        res = 0
        sum_c = 0
        for right ,c in enumerate(calories):
            sum_c += c 
            left = right - k + 1
            if left < 0:
                continue
            if sum_c > upper:
                res += 1
            if sum_c < lower:
                res -= 1
            sum_c -= calories[left]
        return res