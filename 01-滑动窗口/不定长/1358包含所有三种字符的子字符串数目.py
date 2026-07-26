class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        ans = 0
        ch_count = defaultdict(int)
        # 固定右端点，找只出现一次的左端点(left-1)
        for i, ch in enumerate(s):
            ch_count[ch] += 1
            while len(ch_count) == 3 :
                ch_count[s[left]] -= 1
                if ch_count[s[left]] == 0:
                    del ch_count[s[left]]
                left += 1
            ans += left
        return ans