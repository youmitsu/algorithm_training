N = 15
X = 47
A = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]

def search(x):
  L = 1
  R = N
  while L <= R:
    M = int((L + R) / 2)
    if x < A[M]:
        R = M - 1
    if x == A[M]:
        return M
    if x > A[M]:
        L = M + 1
  return -1

answer = search(X)
print(answer)