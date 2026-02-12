```python

""" 
자리 주인을 정하는 방식의 순열
0번 자리에 올 원소 정하기
1번 자리에 올 원소 정하기
...
N-1번 자리에 올 원소 정하기(마지막은 알아서 정해짐)
"""
lst = [1, 2, 3, 4, 5]
N = 5
result = [0] * N
# result = [?, ?, ?, ?, ?]
# idx : 순열의 idx번 자리에 올 원소를 선택하는 중이다
# selected : 순열을 만들때 이전에 사용했던 원소를 체크(중복 선택 방지)
# selected[x] == 1 : x번 원소는 이전에 사용했다
# selected[y] == 0 : y번 원소는 이전에 사용안했다
# result == 만들어진 순열
def make_perm(idx, selected, result):
    # 1. 종료 조건
    # 0번 자리부터 N-1 번 자리까지 다 주인 정했으면 종료    
    if idx == N:
        # 지금까지 만든 순열 출력
        print(result)
        return
    # 2. 재귀 호출
    # idx번 자리에 올 숫자가 누군지 하나 선택
    # 이전에 내가 고른적 없는 숫자만 선택 가능
    for i in range(N):
        # N개의 원소 일일히 확인하며 이전에 사용한 원소면 넘어가
        # 이전에 사용한 적 없는 원소면 idx 자리에 놓고 idx+1번 단계로 진행
        if not selected[i]:
            # idx번 자리에 i번 원소를 놓고 진행
            selected[i] = 1
            # 순열 만들기
            result.append(lst[i])
            # i번 원소를 idx번 자리에 놓고 나머지 경우의 수 고려
            make_perm(idx + 1, selected, result)
            # i번 원소는 다음 자리에서 또 쓸 수 있도록 기록 제거
            selected[i] = 0
            result.pop()

# 0번 자리부터 정하기 시작
# 아직 아무것도 고르지 않은 상태
# 순열은 미완성 상태
make_perm(0, [0] * N, [])

```