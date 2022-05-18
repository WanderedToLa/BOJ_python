b = []

for i in range(9):
    n = int(input())
    b.append(n)
print(max(b))
print(b.index(max(b)) + 1)