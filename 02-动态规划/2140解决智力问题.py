class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        #子问题定义为从i 题question开始（包含第i题）到考试结束内可以获得的最高分数
        # 正向递归
        n = len(questions)
        
        @cache
        def dfs(i:int) -> int:
            if i >= n:
                return 0
            points, brainpower = questions[i]
            skip = dfs(i+1)
            solve = points + dfs(min(i+brainpower+1, n))
            return max(skip, solve)
        
        return dfs(0)
        