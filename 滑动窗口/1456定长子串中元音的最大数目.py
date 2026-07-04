class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # 定长滑动窗口
        ans = 0
        vowel = 0
        for right,c in enumerate(s):
            if c in "aeiou":
                vowel += 1
            left = right - k + 1
            if left < 0:
                continue
            ans = max(ans, vowel)
            if s[left] in "aeiou":
                vowel -= 1
        return ans
