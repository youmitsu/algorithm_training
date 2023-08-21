N = int(input())
a = list(map(int, input().split()))
aliceSum = 0
bobSum = 0
a.sort(reverse=True)
for (i, x) in enumerate(a):
    if (i % 2 == 0):
        aliceSum += x
    else:
        bobSum += x

print(aliceSum - bobSum)
