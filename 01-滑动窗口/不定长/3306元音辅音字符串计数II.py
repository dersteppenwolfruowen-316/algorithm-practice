class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        left1 = left2 = 0 
        sum1 = sum2 = 0 #统计辅音
        y1 = defaultdict(int) #统计元音
        y2 = defaultdict(int) # 不能写y1 = y2
        ans = 0
        for right, w in enumerate(word):
            if w in "aeiou":
                y1[w] += 1
                y2[w] += 1
            else:  #注意是else而不是每个字母都加
                sum1 += 1 
                sum2 += 1
            while sum1>=k and len(y1) == 5 and left1 <= right:
                if word[left1] in "aeiou":
                    y1[word[left1]] -= 1
                    if y1[word[left1]] == 0:
                        del y1[word[left1]]
                else:  #不要忘记辅音的处理
                    sum1 -= 1 
                left1 += 1
            while sum2 >= k+1 and len(y2) == 5 and left2 <= right :
                if word[left2] in "aeiou":
                    y2[word[left2]] -= 1
                    if y2[word[left2]] == 0:
                        del y2[word[left2]]
                else:
                    sum2 -= 1
                left2 += 1
            ans += left1 - left2
        return ans
                

        