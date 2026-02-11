# 1953_탈주범 검거_BFS

> **사용 기술**: `BFS(너비 기반 검색)`, `queue`  

## 코드
```python
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
    visited[i][j] = 1                       # 도둑이 출발한 자리 표시
    count = 1                               # 도둑이 갈 수 있는 칸 수

    while queue:
        i, j, curr_time = queue.popleft()   

        if curr_time >= L:                  # 시간이 L 이상이면 아래 조건문 실행 안함
            continue

        for d in pipe[tunnel_list[i][j]]:   # 다음 갈 수 있는 칸 확인
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if is_connected(d, tunnel_list[ni][nj]):    # 다음 칸과 연결되어있는지 확인
                    visited[ni][nj] = 1                     # 다음 칸 방문 체크
                    queue.append((ni, nj, curr_time + 1))   # 이거 보니까 큐에 튜플로
                                                            # 좌표와 시간값을 넣는듯
                    count += 1                              # 방문한 칸 수 증가
    return count


for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel_list = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]                   # 터널의 크기만큼 방문 리스트 생성

    print(f"#{tc} {bfs(R, C, L)}")
```

## 해결 과정

- 어제 풀었던 [2105_디저트카페](https://github.com/0202Jason/Algorithm/tree/master/SWEA/SWEA_Advanced/260209/2105_dessert(dfs%2C%20recur)) 문제를 생각하고 깊이 기반 검색을 했다가 모든 경우의 수를 다 탐색해서 난감했다.
- 이후 AI 도움을 받아 `queue`를 사용하는 방법과 `queue`에 (좌표, 시간값)을 튜플로 넣고 빼며 카운트를 올리는 로직을 구현하였다.

## AI 활용 과정

### 아이디어 생성
![아이디어](./idea.png)  

### 초안 작성
![초안](./introduction.png)

### `queue` 생성 도움
![도움](./help1.png)

### `queue` 디버깅 도움
![디버깅](./debug.png)

### 로직 설명
![로직1](logic1.png)  
![로직2](logic2.png)