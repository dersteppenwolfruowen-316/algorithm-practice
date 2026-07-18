class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        #倒序滑动窗口更好计算
        #字符串哈希
        n = len(s)
        p = pow(power, k - 1, modulo)
        h = ans_left = 0

        for i in range(n-1,-1,-1):
            # 左端点进入，加法
            h = (h*power + (ord(s[i]) & 31)) % modulo
            right = i + k - 1
            if right >= n:
                continue
            if h == hashValue:
                ans_left = i 
            # 右端点离开，减去
            h = (h-(ord(s[right]) & 31) * p) % modulo
        return s[ans_left: ans_left + k]
            


        
