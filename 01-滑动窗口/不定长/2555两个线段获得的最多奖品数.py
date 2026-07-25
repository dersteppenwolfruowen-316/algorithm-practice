class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        if k * 2 + 1 >= prizePositions[-1] - prizePositions[0]:
            return n
        left = 0
        ans = 0
        prize = [0]*(n+1)
        #不相交覆盖更多
        #前缀最优值，在0-lefti之间用一个线段k能够覆盖的最大奖品数
        #而lefti就是第二条线段的数组左端点
        for i, pos in enumerate(prizePositions):
            left_pos = prizePositions[left]
            while (pos - left_pos) > k and left < i:
                left += 1
                left_pos = prizePositions[left]
            ans = max(ans, prize[left] + i - left + 1)
            # i-left+1是[0,i+1]间一个新值，因此要进行更新
            prize[i + 1] = max(prize[i], i - left + 1)
        
        return ans

