import sys
s = int(sys.stdin.readline())
n = 0
result = 0

while True:
    n += 1
    result += n
    if result > s:
        n -= 1
        break
print(n)