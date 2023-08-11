N = 4
K = 10
A = [1, 2, 3, 4]

def check(x):
  num = 0
  for i in range(N):
    num += int(x / A[i])
  if num >= K:
    return True
  return False

left = 0
right = 1000000000

while (left < right):
  mid = int((left + right) / 2)
  if check(mid):
    right = mid
  else:
    left = mid + 1

print(left)