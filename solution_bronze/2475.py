a = list(map(int, input().split()))
n = 0
for i in a:
    n += i*i
 
print(n % 10)