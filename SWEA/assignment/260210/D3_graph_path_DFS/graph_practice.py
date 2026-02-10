import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

def dfs(start, goal, graph, visited):
    if start == goal:
        return 1
    visited[start] = 1

    for next in graph[start]:
        if not visited[next]:
            if dfs(next, goal, graph, visited):
                return 1
    return 0

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph_map = [[] for _ in range (V+1)]

    for _ in range(E):
        u, v = map(int, input().split())
        graph_map[u].append(v)

    S, G = map(int, input().split())
    visited_list = [0] * (V + 1)
    answer = dfs(S,G, graph_map, visited_list)


    print(f'#{tc} {answer}')