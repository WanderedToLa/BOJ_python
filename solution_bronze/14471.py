n , m = map(int,input().split())
cnt = 0
arr = []
for _ in range ( m ):
    ai , bi = map(int, input().split())
    if ai >= n : cnt += 1
    else: arr.append( (n-ai))
arr = sorted(arr)
if cnt >= m-1: print(0)
else: print(sum(arr[:m - cnt - 1]))