# n = int(input())
# cnt = 0
# second_cnt = 0
# print(n // 2)

# while 1 <= n:
#     if n == 1:
#         print(n)
#         break
#     if (n % 2 != 0) or (n % 3 != 0): #2와 3으로 나누어떨어지지 않을때
#         n -= 1
#     if n % 2 == 0:
#         n = n // 2

n = int(input())
d = [0] * 1000001

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)

    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

print(d[n])