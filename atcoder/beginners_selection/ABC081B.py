N = int(input())
A = list(map(int, input().split()))

count = 0

while(True):
  exist_odd = False
  for i in range(N):
    if (A[i] % 2 != 0): exist_odd = True

  if (exist_odd): break

  for i in range(N):
    A[i] /= 2

  count += 1

print(count)