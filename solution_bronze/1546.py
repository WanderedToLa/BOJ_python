n = int(input())
m = list(map(int , input().split()))
maxValue = max(m)

for i in range(n):
    m[i] = m[i] / maxValue *100

print("%.2f" % (sum(m) / n))