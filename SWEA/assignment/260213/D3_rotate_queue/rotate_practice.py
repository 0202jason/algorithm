import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    q = [0] * (N + M + 100)
    rear = front = -1

    for _ in range(M // N + 1):
        for j in range(N):
            rear += 1
            q[rear] = arr[j]

    for j in range(M):
        front += 1

    print(f"#{tc} {q[front + 1]}")
