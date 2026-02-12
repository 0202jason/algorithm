"""
아이디어: 행`row`값과 현재까지의 숫자 합`sum`을 함수의 변수로 사용하여
재귀를 만들고자 하였다.
AI 도움: visited 인스턴스를 원래 행렬로 만들었는데 열 값만 저장하는 리스트로
바꾸는 아이디어를 받아서 사용했다. 그리고 재귀가 일어나기 전에

if num > matrix[row][j]:
    visited[j] = 1

라고 조건문을 넣었는데 이게 필요가 없어서 제거하는 피드백을 받았다.
재귀식 마지막에 다시 visited[0]을 넣는 것을 도움 받았다.
"""

import sys

sys.stdin = open("sample_input(1).txt", "r")

T = int(input())


def lst_sum(row, sum):      # row와 sum을 함수의 매개변수로 사용
    global min_sum
    # idx가 N층까지 탐색하면 sum을 min 값과 비교
    if row == N:
        if min_sum > sum:
            min_sum = sum
        return
    # sum이 이미 min_sum보다 크다면 실행 종료(가지치기)
    if sum > min_sum:
        return
    """
    N번째 행에서의 최솟값을 각각 찾아서 min_list에 추가한다
    """

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            # 잘못된 코드
            # if num > matrix[row][j]:
            #    visited[j] = 1
            lst_sum(row + 1, sum + matrix[row][j])
            visited[j] = 0


for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_sum = 999999
    lst_sum(0, 0)
    print(f"#{tc} {min_sum}")
