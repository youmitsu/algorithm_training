s1,s2,s3 = input()

def check(x):
  return x == '1'

count = 0
count += 1 if check(s1) else 0
count += 1 if check(s2) else 0
count += 1 if check(s3) else 0

print(count)
