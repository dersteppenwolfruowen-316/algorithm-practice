class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = [0]*121 #存储各个年龄段有多少个人
        for x in ages:
            cnt[x] += 1
        
        ans = cnt_window = age_y = 0
        for age_x, c in enumerate(cnt):
            cnt_window += c 
            if age_y * 2 <= age_x + 14:
                cnt_window -= cnt[age_y]
                age_y += 1
            if cnt_window:
                ans += c * cnt_window - c # c个用户可以给窗口内的全部用户发消息，但要减去给自己的
        return ans



        