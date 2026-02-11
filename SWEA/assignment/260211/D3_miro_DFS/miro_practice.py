T = int(input())

di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]

for tc in range(1, T+1):
    N = int(input())
    num_list = [(input()) for _ in range(N)]
    answer = 0
    matrix = [[0]*N for _ in range(N)]

    for i in range(N):                              # 리스트를 2차원으로 변환
        for j in range(N):
            matrix[i][j] = int(num_list[i][j])

    for i in range(N):                              # 시작점 2의 인덱스 찾기
        for j in range(N):
            if matrix[i][j] == 2:
                si, sj =i, j

    stack = [(si, sj)]                              # 시작점 스택, 방문리스트에 넣기
    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 1

    while stack:                                    # 스택이 비면 종료
        ci, cj = stack.pop()                        # 첫 위치 팝
        if matrix[ci][cj] == 3:                     # 3을 뱉으면 종료
            answer = 1
            break

        for d in range(4):                          # 델타 탐색
            ni = ci + di[d]                         # 주변에 0 혹은 3이 있으면 스택에 추가, 방문 표시
            nj = cj + dj[d]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if matrix[ni][nj] == 0 or matrix[ni][nj] == 3:
                    stack.append((ni, nj))
                    visited[ni][nj] = 1

    print(f"#{tc} {answer}")
