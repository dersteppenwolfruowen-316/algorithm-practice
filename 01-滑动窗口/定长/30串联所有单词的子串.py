class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        x = len(words[0])
        k = len(words) * x
        
        words_cnt = Counter(words)
        ans = []
        #相当于不同的起点,转化为滑动窗口，只需计算in和out，中间可以不变
        #总结：转化为滑动窗口的要点
        for i in range(x):
            s_cnt = defaultdict(int)
            overload = 0 #统计过多和不在words中的单词
            for right in range(i+x, len(s)+1, x):
                in_word = s[right-x:right]
                if s_cnt[in_word] == words_cnt[in_word]:
                    overload += 1
                s_cnt[in_word] += 1

                left = right - k
                if left < 0:
                    continue

                if overload == 0:
                    ans.append(left)

                out_word = s[left:left + x]
                s_cnt[out_word] -= 1
                if s_cnt[out_word] == words_cnt[out_word]:
                    overload -= 1

        return ans
