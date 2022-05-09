# h , m = map(int , input().split())

# if m > 45:
#     print(h , m - 45)
# elif h > 0 and m < 45:
#     print(h -1 , m + 15)
# else:
#     print(23 , m + 15)

H, M = map(int, input().split())

if M < 45 :	# 분단위가 45분보다 작을 때 
    if H == 0 :	# 0 시이면
        H = 23
        M += 60
    else :	# 0시가 아니면 (0시보다 크면)
        H -= 1	
        M += 60
        
print(H, M-45)