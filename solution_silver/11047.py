n , k = map(int , input().split())
a = []
cnt = 0

for i in range(n):
    coin = int(input())
    a.append(coin)

for i in range(n - 1 , -1 , -1):
    if k == 0:
        break
    if a[i] > k:
        continue
    cnt += k // a[i]
    k = k % a[i]
print(cnt)