lst = [1, 2, 3, 4, 5]
N = 5

# idx : idx번 자리에 있는 원소의 자리를 교환하겠다
def make_perm(idx):

    # 1. 종료 조건
    if idx == N:
        print(lst)
        return


    # 2. 재귀 호출
    # idx번 원소와 다른 위치에 있는 원소를 하나 정하고
    # 자리를 바꾼다. 다른 위치(j)의 조건 idx보다 작으면 안된다.
    for j in range(idx, N):
        # idx번 원소와 j번 원소 자리를 바꾸겠다.
        lst[idx], lst[j] = lst[j], lst[idx]
        make_perm(idx + 1)
        lst[idx], lst[j] = lst[j], lst[idx]

make_perm(0)
