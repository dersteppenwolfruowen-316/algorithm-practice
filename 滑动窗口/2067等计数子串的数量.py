class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        ans = 0
        for x in range(1,27):
            k = x * count # 子串长度是字母种类乘以count
            if k > len(s):
                break
            letter_count = defaultdict(int)
            valid_chars = 0
            for right, c in enumerate(s):
                letter_count[c] += 1
                left = right - k + 1
                if letter_count[c] == count:
                    valid_chars += 1
                elif letter_count[c] == count + 1:
                    valid_chars -= 1
                if left < 0:
                    continue
                if valid_chars == x and len(letter_count) == x:
                    ans += 1
                if letter_count[s[left]] == count:
                    valid_chars -= 1
                elif letter_count[s[left]] == count + 1:
                    valid_chars += 1
                letter_count[s[left]] -= 1 
                if letter_count[s[left]] == 0:
                    del letter_count[s[left]]
        return ans          



        
        