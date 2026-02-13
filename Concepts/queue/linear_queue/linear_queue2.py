# 느려서 못씀

q = []

for i in range(1, 11):
    q.append(i)

print(q)

for i in range(10):
    e = q.pop(0)
    print(e, end=" ")
print()
