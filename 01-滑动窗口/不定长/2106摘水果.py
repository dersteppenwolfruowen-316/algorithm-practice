class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = 0
        ans = 0
        s = 0
        length = 0
        # 只需要判断k步内，能走到哪几个pos
        for right in range(len(fruits)):
            #计算走到窗口内这些点需要的最小步长
            s += fruits[right][1]
            while left <= right:
                # 两种走法
                length = min(abs(fruits[right][0]-startPos), abs(fruits[left][0]-startPos) )+fruits[right][0] - fruits[left][0]
                if length <= k:
                    break
                s -= fruits[left][1]
                left += 1
            ans = max(ans, s)
        return ans