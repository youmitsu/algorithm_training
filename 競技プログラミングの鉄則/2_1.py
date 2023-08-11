N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = [0] * Q
R = [0] * Q
for i in range(Q):
    L[i], R[i] = map(int, input().split())

list = []
sum = 0
for a in A:
    sum += a
    list.append(sum)

print(list)

for i in range(Q):
    print(list[R[i] - 1] - list[L[i] - 2])
