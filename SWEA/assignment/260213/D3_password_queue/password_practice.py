import sys

sys.stdin = open("input (3).txt", "r")

T = 10


for tc in range(1, T + 1):
    N = int(input())
    password = list(map(int, input().split()))
    while password[7] != 0:
        for i in range(0, 5):
            temp = password.pop(0)
            if (temp - (i + 1)) <= 0:
                password.append(0)
                break
            else:
                password.append(temp - (i + 1))

    print(f"#{tc}", *password)
