> 언어: Python  
> 메모리: 60,288 kb     
> 실행시간: 99 ms  

```python
"""
나의 생각: 한 줄씩 가로 세로 다 보면서 오르막길이 놔지는지 확인하면 될듯
for 문으로 싹 다 돌리면 될 것 같다.
오르막의 시작점 앞에는 턱이 없어야하고, 오르막이 끝난 후에도 턱이 있으면 안된다
AI 생각: 오르막을 설치할 수 있는지 체크하는 부분을 함수를 만들어서
가로, 세로 체크할 때 재활용해라.
경사로를 설치할 수 없는 단 하나의 경우의 수가 있어도 그 행, 열은 그냥 False 처리하면 된다.
"""

T = int(input())


def check(line, N, X):

    visited = [0] * N  # 경사로가 이미 설치되었는지 확인

    for i in range(N - 1):
        # 높이가 같은 경우 통과
        if line[i] == line[i + 1]:
            continue

        # 높이 차이가 1보다 큰 경우 건설 불가능
        if abs(line[i] - line[i + 1]) > 1:
            return False

        # 내리막길
        if line[i] > line[i + 1]:
            # 경사로 길이 X 만큼 검사
            for j in range(i + 1, i + 1 + X):
                # 범위를 벗어나거나, 높이가 일정하지 않거나, 이미 경사로가 있으면 안됨
                if j >= N or line[j] != line[i + 1] or visited[j]:
                    return False
                # 경사로 설치
                visited[j] = 1

        # 오르막길을 만난 경우
        elif line[i] < line[i + 1]:
            # 경사로 길이 L만큼 뒤를 체크
            for j in range(i, i - X, -1):
                # 범위를 벗어나거나, 높이가 일정하지 않거나, 이미 경사로가 있으면 안됨
                if j < 0 or line[j] != line[i] or visited[j]:
                    return False
                visited[j] = 1  # 경사로 설치 표시냥!

    return True


for tc in range(1, T + 1):
    N, X = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    # 행 방향 검사
    for i in range(N):
        if check(matrix[i], N, X):
            answer += 1

    # 열 방향 검사
    for j in range(N):
        # 열 방향 리스트 생성
        col_lst = [matrix[i][j] for i in range(N)]
        if check(col_lst, N, X):
            answer += 1

    print(f"#{tc} {answer}")
```