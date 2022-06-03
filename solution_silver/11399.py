n = int(input())
p = list(map(int , input().split()))
sum = 0
time = 0
p.sort()

for i in p:
    sum += i
    time += sum
print(time)