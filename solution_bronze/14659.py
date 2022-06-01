# 반복문을 통해서 리스트의 요소를 하나씩 검사하고 다음 요소가 전보다 작으면 +1 증가 크다면 0으로 초기화
n = int(input())
high = list(map(int , input().split()))
kill_cnt = 0
#다음 요소의 크기를 판별하면 해결 가능할듯
for i in range(n):
    if high[i:] < high[i + 1:]:
        kill_cnt = 0
    elif high[i:] > high[i + 1:]:
        kill_cnt += 1
print(kill_cnt)