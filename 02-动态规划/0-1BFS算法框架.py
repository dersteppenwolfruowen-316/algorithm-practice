from collections import deque

def zero_one_bfs(start, graph, n):
    dist = [inf] * n
    dist[start] = 0
    dq = deque([start])
    
    while dq:
        u = dq.popleft()
        for v, w in graph[u]:   # w 是 0 或 1
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if w == 0:
                    dq.appendleft(v)   # 权重0，插到队首
                else:
                    dq.append(v)       # 权重1，插到队尾
    return dist