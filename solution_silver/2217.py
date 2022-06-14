n = int(input())
a = []

for i in range(n):
    w = int(input())
    a.append(w)

a.sort(reverse=True)

b = []

for i in range(n):
    b.append(a[i] * (i + 1))
print(max(b))