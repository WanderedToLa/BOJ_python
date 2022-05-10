A,B = map(int , input().split())
C = int(input())
B += C

if B >= 60:
    A += B // 60
    B -= 60
    if B % 60 == 0:
        B = 0
    if A == 24:
        A -= 24
print(A , B)

# h, m = map(int, input().split())
# t = int(input()) 

# h += t // 60
# m += t % 60

# if m >= 60:
#     h += 1
#     m -= 60
# if h >= 24:
#     h -= 24

# print(h, m)