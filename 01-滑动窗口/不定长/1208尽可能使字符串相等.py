class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # 转化开销maxcost的最长子字符串
        cost = 0
        ans = 0
        left = 0
        for i in range(len(s)):
            cost += abs(ord(s[i]) - ord(t[i]))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, i - left + 1)
        return ans 

        