class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        
        n = len(s)
        pairs = 0
        left = 0
        ans = 0
        for i in range(len(s)):
            if i>0 and s[i-1] == s[i]:
                pairs += 1
            while pairs > 1:
                if s[left] == s[left+1]:
                    pairs -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans 
            


        