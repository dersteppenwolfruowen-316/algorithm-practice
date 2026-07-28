class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        # 也就是找出子字符串包含word2的字符
        if len(word1) < len(word2):
            return 0
        total_ch = Counter(word2)
        left = 0 
        ans = 0
        ch = defaultdict(int)
        valid = 0
        for right, s in enumerate(word1):
            if s in word2:
                ch[s] += 1
                if ch[s] == total_ch[s]:
                    valid += 1
            while valid == len(total_ch) and left <= right:
                if word1[left] in word2:
                    ch[word1[left]] -= 1
                    if ch[word1[left]] < total_ch[word1[left]]: #注意是小于，已经去掉了一个left
                        valid -= 1
    
                left += 1
            ans += left
        return ans 
        