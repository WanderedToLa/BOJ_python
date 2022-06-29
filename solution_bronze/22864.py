a, b, c, m = map(int, input().split())

day = 0
result = 0
cnt = 0

if a > m :
    print(0)
else :
    while day != 24 :
        day += 1
        if cnt + a <= m :
            result += b
            cnt += a
        else :
            if cnt - c >= 0 :
                cnt -= c
            else :
                cnt = 0
    print(result)