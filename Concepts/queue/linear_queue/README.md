# 선형 큐(Linear Queue)

### 코드

```python 
# front, rear 사용

N = 10
q = [0] * N

front = rear = -1

for i in range(1, 11):
    rear+=1
    q[rear] = i

    print(q)
    print(front, rear)

for i in range(1, 10):
    front+=1
    print(q[front], end = " ")
print()

print(q)
print(front, rear)
```