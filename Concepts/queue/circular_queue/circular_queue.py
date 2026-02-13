N = 10

cq = [0] * N
front = rear = 0
# 원형큐는 공백과 포화 상태 구분을 위해
# front 자리를 한 개 비워둔다.

def is_full():
    return (rear + 1) % N == front

for i in range(1, 11):
    if not is_full():
        rear = (rear + 1) % N
        cq[rear] = i

print(cq)
print(front, rear)

for i in range(9):
    front = (front + 1) % N
    print(cq[front], end=" ")
print()

print(cq)
print(front, rear)