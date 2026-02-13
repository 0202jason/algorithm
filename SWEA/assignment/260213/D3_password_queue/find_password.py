T = 10


for tc in range(1, T + 1):
    N = int(input())
    password = list(map(int, input().split()))      # 입력 받은 리스트. 큐로 사용
    while password[7] != 0:                         # 마지막 패스워드가 0이 되면 종료
        for i in range(0, 5):               
            temp = password.pop(0)                  # 앞의 수를 i만큼 빼서
            if (temp - (i + 1)) <= 0:               # 맨 뒤에 추가한다
                password.append(0)                  # pop한 숫자에 i를 빼서 0보다 작으면
                break                               # 종료 조건을 맞춘다
            else:
                password.append(temp - (i + 1))

    print(f"#{tc}", *password)
