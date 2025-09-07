from collections import deque

N = int(input()) # 정점 수

nodes = [[] for i in range(N + 1)] # 0번 인덱스를 안 쓸겁니다.
# 현재 정점이 갈 수 있는 정점들을 저장

# (u, v)

for i in range(N - 1):
    # node = list(map(int, input().split())) # i + 1 번째 정점이 갈 수 있는 정점들
    # nodes[i + 1] = node
    
    u, v = map(int, input().split())
    
    nodes[u].append(v)
    nodes[v].append(u)

# print(*nodes, sep="\n")

visited = [False] * (N + 1) # 0번 안 씀

# def dfs(cur): # cur는 현재 정점
#     print(cur, '->', end = "")
    
#     for child in nodes[cur]:
#         if visited[child]: continue # 방문한 상태이면 중복 방문을 하지 않는다.
        
#         visited[child] = True # 방문한 상태로 바꿔준다.
#         dfs(child)

# visited[1] = True
# dfs(1)

que = deque()
que.append(1)

visited[1] = True

while que:
    cur = que.popleft()
    print(cur, "->", end = " ")
    
    for child in nodes[cur]:
        if visited[child]: continue
        
        visited[child] = True
        que.append(child)