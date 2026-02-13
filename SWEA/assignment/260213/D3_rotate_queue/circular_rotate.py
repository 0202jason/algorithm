import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

front = rear = 0

def is_full():
    return(rear + 1) % N == front


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    cq = [0] * (N + 1)

    for i in range(0, N):
        if not is_full():
            rear = (rear + 1) % N
            cq[rear] = arr[i]
    print(cq)
    