class Solution:
    def minFlips(self, s: str) -> int:
        #s+s[:-2]每一个子串统计变为'010...'和'101..'的最小值,子串便可用滑动窗口
        #cnt统计'1010...','0101..'就是n-cnt
        ans = n = len(s)
        cnt = 0 
        for i in range(n*2-1):
            if ord(s[i%n]) % 2 != i%2:
                cnt += 1
            left = i - n + 1
            if left < 0:
                continue
            ans = min(ans,cnt,n-cnt)
            if ord(s[left]) % 2 != left % 2:
                cnt -= 1
        return ans





        