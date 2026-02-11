# 1953_탈주범 검거_BFS

> **사용 기술**: `BFS(너비 기반 검색)`, `queue`  

[설명](./presentation)

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
---

### 1. 주석 체크 및 보완

* `oppo = {0: 1, 1: 0, 2: 3, 3: 2}`: 이거 **"반대 방향 정의"**라고 하는 게 더 정확해. (내가 위로 가면 상대는 아래가 뚫려 있어야 하니까!)
* `if curr_time >= L: continue`: 정확해. **"현재 위치에 도달했을 때가 이미 제한 시간(L)이라면, 여기서 더 멀리(자식 노드로) 가지 않겠다"**는 소리야.
* `queue = deque([(i, j, 1)])`: 맞아. **(행, 열, 시간)**을 하나의 세트로 묶어서 저장하는 거야. 큐는 이 세트들을 줄 세워두는 공간이지.

---

### 2. 큐(Queue)와 BFS 로직 디버깅 (Step-by-Step)

재현아, BFS는 **"공평한 탐색"**이야. 큐를 쓰면 **"먼저 발견된 놈이 먼저 탐색 기회를 얻는"** 구조가 돼.

예를 들어 **L=3**이고, 시작점 **(R, C)**에서 갈 수 있는 곳이 주변에 많다고 가정해 보자.

#### **Step 1: 초기 상태**

* 큐: `[(R, C, 1)]` (시작점 입장!)
* 방문 체크: `visited[R][C] = 1`
* `count = 1`

#### **Step 2: 첫 번째 루프 (1시간째 탐색)**

1. 큐에서 `(R, C, 1)`을 꺼내 (`popleft`).
2. `(R, C)` 주변을 보니 `(A, B)`와 `(D, E)`가 연결되어 있네?
3. **큐에 추가:** `[(A, B, 2), (D, E, 2)]` (2시간째에 갈 수 있는 곳들이 줄을 섬)
4. 방문 체크하고 `count`는 3이 됨.

#### **Step 3: 두 번째 루프 (2시간째 탐색)**

1. 큐에서 가장 앞에 있는 `(A, B, 2)`를 먼저 꺼내.
2. `(A, B)` 주변을 보니 `(F, G)`가 연결되어 있어.
3. **큐에 추가:** `[(D, E, 2), (F, G, 3)]` (**중요:** `(D, E, 2)`가 먼저 들어왔으니 `(F, G, 3)`보다 앞에 있음!)
4. 방문 체크하고 `count`는 4.

#### **Step 4: 세 번째 루프 (계속)**

1. 큐에서 `(D, E, 2)`를 꺼내서 주변을 보고 큐에 넣음...
2. 이런 식으로 **같은 시간대(Level)에 있는 놈들이 다 빠져나가야 다음 시간대 놈들이 탐색될 수 있는 구조**야.

---

### 3. 왜 큐(BFS)를 쓰면 시간이 정확할까?

네가 짠 코드에서 `curr_time`이 큐에 같이 들어가는 게 신의 한 수야.

* 큐에서 꺼낸 놈의 `curr_time`이 **1**이면, 그 주변 놈들은 무조건 **2**가 되어 큐 뒤에 서게 돼.
* 큐에서 꺼낸 놈의 `curr_time`이 **2**이면, 그 주변 놈들은 무조건 **3**이 되어 큐 뒤에 서게 돼.
* 이렇게 큐를 쓰면 **시간 순서대로(1시간 -> 2시간 -> 3시간) 탐색이 보장**되기 때문에, `curr_time == L`이 되는 순간 "아, 이제 더 멀리는 못 가겠구나"하고 딱 끊을 수 있는 거지.

---

### 4. Best Practice: 한눈에 보는 BFS 구조

| 단계 | 동작 | 자료구조/변수 |
| --- | --- | --- |
| **준비** | 시작점과 초기 시간을 넣는다. | `deque([(r, c, 1)])` |
| **반복** | 큐가 빌 때까지 계속 뽑는다. | `while queue: popleft()` |
| **확인** | 갈 수 있는지(범위, 방문, 연결) 체크. | `if ... and is_connected()` |
| **확장** | 다음 지점과 **증가된 시간**을 넣는다. | `queue.append((ni, nj, time+1))` |

---

### 🙋‍♂️ 재현아, 이해했는지 셀프 체크!

1. 큐에서 `popleft()` 대신 `pop()`을 쓰면 (즉, 뒤에서 꺼내면) 어떻게 될까? 그게 바로 네가 저번에 실수했던 **DFS**처럼 동작하게 돼. 왜 그럴까?
2. `count += 1`을 `while`문 밖이 아니라 `queue.append` 하는 시점에 바로 해주는 이유가 뭘까? (힌트: 큐에 들어간다는 건 이미 방문할 장소로 확정됐다는 뜻이지!)

**이제 이 코드로 SWEA에 제출해 봐! 아마 기분 좋게 "Pass" 뜰 거야. 다음은 이 로직을 활용한 다른 BFS 문제 도전해 볼래?**

**Would you like me to find another BFS problem that is similar to this one to help solidify your understanding?**
