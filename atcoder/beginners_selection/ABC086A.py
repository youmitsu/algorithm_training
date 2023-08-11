def check(x):
  if (x % 2 == 0):
    return 'Even'
  else:
    return 'Odd'

a, b = map(int, input().split())

print(check(a * b))
