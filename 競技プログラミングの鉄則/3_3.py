N = 7
K = 10
A = [11, 12, 16, 22, 27, 28, 31]
R = [0] * N

for i in range(N):
    if (i == 0): R[i] = 1
    else: R[i] = R[i - 1]

    while(R[i] < N and A[R[i] + 1] - A[i] <= K):
        R[i] += 1

answer = 0
for i in range(N):
    answer += R[i] - i