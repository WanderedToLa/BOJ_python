n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

for i in range(n) :
    a[i] = a[i] + i + 1

print(max(a) + 1)