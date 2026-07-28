class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        left = ans = start = 0
        ch_count = defaultdict(int)
        for right, w in enumerate(word):
            if w not in "aeiou":
                ch_count.clear() 
                start = left = right + 1 # 辅音直接跳过
                continue

            ch_count[w] += 1
            while len(ch_count) == 5 :
                ch_count[word[left]] -= 1
                if ch_count[word[left]] == 0:
                    del ch_count[word[left]]
                left += 1
            ans += left - start # 仅由元音，因此要记录元音开始的start
        return ans
        