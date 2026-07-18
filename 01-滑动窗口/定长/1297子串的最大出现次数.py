class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        k = minSize
        chr_c = ''
        chr_count = defaultdict(int)
        substr = defaultdict(int)
        for r,c in enumerate(s):
            chr_c += c
            chr_count[c] += 1
            left = r - k + 1
            if left < 0:
                continue
            # 注意是不同字母数，而不是同一字母的重复数
            if len(chr_count) <= maxLetters:

                substr[chr_c] += 1
            chr_c = chr_c[1:]
            chr_count[s[r-k+1]] -= 1
            if chr_count[s[r-k+1]] == 0:
                del chr_count[s[r-k+1]]
        return max(substr.values()) if substr else 0
        