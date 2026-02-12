T = int(input())


def lst_sum(row, sum):
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
    num = matrix[0][0]
    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            #잘못된 코드
            #if num > matrix[row][j]:
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

