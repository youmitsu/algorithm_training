n, a, b = map(int, input().split())

result = 0
for i in range(1, n + 1):
    sum = 0
    for x in list(str(i)):
        sum += int(x)
    if (a <= sum and sum <= b):
        result += i
print(result)
