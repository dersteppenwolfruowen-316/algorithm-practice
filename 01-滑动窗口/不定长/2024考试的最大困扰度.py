class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # 包含k个t的最长子数组或k个f的最长子数组
        left = 0
        answer_count = defaultdict(int)
        ans = 0
        for i in range(len(answerKey)):
            answer_count[answerKey[i]] += 1
            while answer_count['T'] > k and answer_count['F'] > k:
                answer_count[answerKey[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans
