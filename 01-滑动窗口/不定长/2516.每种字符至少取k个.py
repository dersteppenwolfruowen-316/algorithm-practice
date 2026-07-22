class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        ch_count = defaultdict(int)
        total_count = defaultdict(int)
        for i in s:
            total_count[i] += 1
        for ch in 'abc':
            if total_count[ch] < k:
                return -1
        left = 0
        ans = -1
        for right in range(len(s)):
            ch_count[s[right]] += 1
            while (ch_count['a'] > total_count['a'] - k or ch_count['b'] >  total_count['b'] - k or ch_count['c'] >  total_count['c'] - k) :
                ch_count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return len(s) - ans 

        