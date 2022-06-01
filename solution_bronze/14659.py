# 반복문을 통해서 리스트의 요소를 하나씩 검사하고 다음 요소가 전보다 작으면 +1 증가 크다면 0으로 초기화
# 6 4 10 2 5 7 11
# n = int(input())
# high = list(map(int , input().split()))
# kill_cnt = 0
# idx = 1
# 다음 요소의 크기를 판별하면 해결 가능할듯
# for i in high:
#     if high[idx] > len(high):
#         break
#     if i > high[idx]:
#         kill_cnt += 1
#         high.pop()
#     elif i < high[idx]:
#         kill_cnt = 0
#     idx += 1
# print(kill_cnt , high)

n = int(input())
h = list(map(int, input().split()))

i = 0
max = 0
while i < n:
    cnt = 0
    for j in range(i+1, n):
        if h[i] > h[j]:
            cnt += 1
        else:
            break
    if max < cnt:
        max = cnt
    
    i += cnt + 1
print(max)