a = int(input())
b = int(input())
c = int(input())
d = list(str(a * b * c))
e = [0,0,0,0,0,0,0,0,0,0]

for i in d:
    e[int(i)] += 1

for i in e:
    print(i)