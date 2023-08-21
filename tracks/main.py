import sys

def main(lines):
    for i, l in enumerate(lines):
        if (i == 0):
            n = int(l)
        if (i == 1):
            a = list(map(int, l.split()))
        else:
            pass
    aliceSum = 0
    bobSum = 0
    a.sort(reverse=True)
    for (i, x) in enumerate(a):
        if (i % 2 == 0):
            aliceSum += x
        else:
            bobSum += x

    print(aliceSum - bobSum)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)