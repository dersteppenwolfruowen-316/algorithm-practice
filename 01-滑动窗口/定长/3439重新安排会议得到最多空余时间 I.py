
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        # 注意长度是n+1
        all_int = [0] * (n + 1)
        all_int[0] = startTime[0] - 0
        all_int[-1] = eventTime - endTime[-1]
        for i in range(1, n):
            all_int[i] = startTime[i] - endTime[i-1]  
            
        if len(all_int) <= k:
            return sum(all_int)
        int_t = 0
        res = 0
        for i, c in enumerate(all_int):
            int_t += c 
            left = i - k 
            if left < 0:
                continue
            res = max(res, int_t)
            int_t -= all_int[left]
        return res



        

        
        