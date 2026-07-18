class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        ch_count = defaultdict(int)
        left = 0
        for right, i in enumerate(s):
            ch_count[i] += 1
            while ch_count[i] > 1:
                ch_count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
        


        