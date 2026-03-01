"""
나의 생각: 일단 문제를 보자마자 뭐야 ㅈㄴ 쉽네? 완탐 돌린다!!ㅋㅋ
ai의 아이디어: 일단 완탐할게? 묻자마자 일단 집이 있는 좌표들을
리스트에 다 넣어두라고 했음.
마름모의 지름(K)를 N보다 더 크게 해보라는 지시가 있었음.

"""


import sys

sys.stdin = open("small_sample.txt", "r")

T = int(input())




for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 배열을 순회하며 주거 지역(1)의 좌표를 리스트에 사전 등록
    houses = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                houses.append((i, j))
    
    max_house = 0

    # 모든 좌표를 돌며 검사
    for i in range(N):
        for j in range(N):
            # 서비스의 크기를 N+1까지 탐색
            for k in range(1, N + 2):
                cost = k * k + (k - 1)*(k - 1)
                count = 0

                # 마름모 범위(맨하탄 거리 내) 포함 여부 확인
                for y, x in houses:
                    dist = abs(i - y) + abs(j - x)
                    if dist < k:
                        count += 1
                
                # 총 수익(가구수 * M)이 운용 비용 이상일 경우, 최대 수용 가구 수 갱신
                if count * M >= cost:
                    if count > max_house:
                        max_house = count

    print(f"#{tc} {max_house}")                