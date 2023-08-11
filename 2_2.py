D = int(input())
N = int(input())

days = [0] * D

for i in range(N):
    L, R = map(int, input().split())
    for j in range(L - 1, R):
        days[j] += 1

for d in range(D):
    print(days[d])
