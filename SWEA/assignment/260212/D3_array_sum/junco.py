T = int(input())
 
def dfs(row,selected,total):
    global min_value
    # 가지치기
    if total >= min_value:
        return
    # 종료 조건
    if row == N: # 마지막 행에 다다르면 종료
        min_value=min(min_value, total)
        return
    for j in range(N): # 행 순회
        # 아직 j열을 선택하지 않았다면
        if not selected[j]:
            selected[j] = 1
            dfs(row+1,selected,total+arr[row][j])
            selected[j] = 0
for tc in range(1,T+1):
    min_value = float('inf')
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    selected = [0] * N
    # 만든 arr로 순열을 만들어야함.
    # 근데 서로 j 가 겹치지 않게 만들어야함.
 
    dfs(0, selected, 0)
    print(f'#{tc} {min_value}')