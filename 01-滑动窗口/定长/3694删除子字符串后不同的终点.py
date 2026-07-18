class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        
        maps = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
        x = y = 0
        all_p = set()
        for i, r in enumerate(s):
            dx, dy = maps[r]
            x += dx
            y += dy
            
            left = i - k + 1
            if left < 0:
                continue
            all_p.add((x,y))
            dx,dy = maps[s[left]]
            x -= dx
            y -= dy
        return len(all_p)