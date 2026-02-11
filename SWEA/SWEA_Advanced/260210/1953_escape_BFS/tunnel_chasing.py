from collections import deque

T = int(input())

di = [-1, 1, 0, 0]                           # 상하좌우로 델타 배열 생성
dj = [0, 0, -1, 1]

pipe = {                                     # 파이프 종류 별로 갈 수 있는 방향 정의
    0: [],
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [0, 3],
    5: [1, 3],
    6: [1, 2],
    7: [0, 2],
}
oppo = {0: 1, 1: 0, 2: 3, 3: 2}             # 반대 방향 정의(내가 위로가면 상대는 아래가 뚫려야)


def is_connected(d, next):                  # 길이 연결되어있는지 확인
    if next == 0:
        return 0
    return oppo[d] in pipe[next]            # 다음 칸과 길이 연결되어 있는지 함수


def bfs(i, j, L):
    queue = deque([(i, j, 1)])              # 큐를 생성해서 푸는데 이해가 잘 안됨
                                            # 설명: 처음 시작점과 시간값(1)을 
                                            # 최초의 큐 값 튜플로 리스트에 추가한다
    visited[i][j] = 1                       # 도둑이 출발한 자리 방문 표시
    count = 1                               # 도둑이 갈 수 있는 칸 수

    while queue:
        i, j, curr_time = queue.popleft()   # 확인 한 칸은 'pop' 해서 리스트에서 비움

        if curr_time >= L:                  # 시간이 L 이상이면 아래 조건문 실행 안함
            continue

        for d in pipe[tunnel_list[i][j]]:   # 다음 갈 수 있는 칸 확인
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if is_connected(d, tunnel_list[ni][nj]):    # 다음 칸과 연결되어있는지 확인
                    visited[ni][nj] = 1                     # 다음 칸 방문 체크
                    queue.append((ni, nj, curr_time + 1))   # 방문 하지 않은 칸을 큐에 넣어서 'pop' 될 때 까지 기다린다
                                                            # 시간값이 최대가 되면 위의 컨티뉴와 이어짐
                    count += 1                              # 방문한 칸 수 증가
    return count


for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel_list = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]                   # 터널의 크기만큼 방문 리스트 생성

    print(f"#{tc} {bfs(R, C, L)}")
