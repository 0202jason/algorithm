T = int(input())

for tc in range(1, T+1):
    # 미로의 크기 N
    N = int(input())

    # 미로의 정보
    # 0 : 이동 가능
    # 1 : 벽(이동 불가)
    # 2 : 시작 지점
    # 3 : 도착 지점
    maze = [list(map(int, input())) for _ in range(N)]

    si, sj = 0, 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    def dfs(i, j):
        visited = [[0] * N for _ in range(N)]
        stack = []
        visited[i][j] = 1
        i, j = si, sj

        while True:

            if maze[i][j] == 3:
                return 1
            
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and maze[ni][nj] != 1:
                    visited[ni][nj] = 1
                    stack.append((i, j))
                    i, j = ni, nj
                    break
            else:
                if stack:
                    i, j = stack.pop()
                else:
                    break

        return 0

    print(f"#{tc} {dfs(si, sj)}")            