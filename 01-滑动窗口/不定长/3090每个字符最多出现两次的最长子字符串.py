class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        ch_count = defaultdict(int)
        for right,i in enumerate(s):
            ch_count[i] += 1
            while ch_count[i] > 2 and left < right:
                ch_count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans