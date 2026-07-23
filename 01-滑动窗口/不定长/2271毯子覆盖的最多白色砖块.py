class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort(key=lambda x: x[0])
        white = 0
        ans = 0
        left = 0
        for i in range(len(tiles)):
            if tiles[i][1]- tiles[i][0] == carpetLen:
                return carpetLen
        # 右端点一定在白瓷砖最右边
        for l, r in tiles:
            #毯子长度固定,记录两个left
            white += r - l + 1
            carpet_left = r - carpetLen + 1
            while tiles[left][1] < carpet_left:
                white -= tiles[left][1] - tiles[left][0] + 1
                left += 1
            # 没有白色瓷砖，有毯子的部分
            uncover = max(carpet_left - tiles[left][0], 0)
            ans = max(ans, white - uncover)  
        return ans