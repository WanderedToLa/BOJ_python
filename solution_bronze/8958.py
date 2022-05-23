n = int(input())

for i in range(n):
    a = input()
    arr = list(a)
    result = 0
    cnt = 0
    for j in arr:
        if j == 'O':
            cnt += 1
            result += cnt
        elif j == 'X':
            cnt -= cnt
            result += 0
    print(result)