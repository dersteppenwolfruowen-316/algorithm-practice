class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 从左到右单调栈解法
        # 栈存储还没找到最大温度的元素
        n = len(temperatures)
        st = []
        ans = [0]*n
        for i, t in enumerate(temperatures):
            while st and t > temperatures[st[-1]]:
                j = st.pop()
                ans[j] = i - j
            st.append(i) #将目前最高温入栈
        return ans