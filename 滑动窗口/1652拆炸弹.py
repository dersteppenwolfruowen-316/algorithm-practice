class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]*len(code)
        n = len(code)
        code_res = [0]*n
        # 初始窗口的右开端点
        r = k + 1 if k > 0 else n
        k = abs(k)
        s = sum(code[r-k:r]) # 初始窗口和
        # 循环的仍然是结果元素的下标，从0开始，就不会混乱
        for i in range(n):
            code_res[i] = s 
            # 搞清楚移进入窗口元素和出窗口元素下标就可以
            s += code[r%n] - code[(r-k)%n] #加上进入窗口元素，移出出窗口元素
            r += 1
        return code_res


        

        