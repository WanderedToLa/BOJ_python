# 학생들 점수의 평균 구하기 -> 평균보다 높은 인원 / 학생수 -> 결과 x 100 => 평균을 넘는 비율
# c = int(input())
# first = 0
# avg = 0

# for i in range(c):
#     a = list(map(int , input().split()))
#     first = a.pop(0)
#     avg = sum(a) / first
#     percent = 0
#     for i in a:
#         if i < avg:
#             percent += 1
#     percent = (percent / first) * 100
#     print('%.3f'%percent+'%')

c = int(input())

for i in range(c):
    a =list(map(int , input().split()))
    avg = sum(a[1:]) / a[0]
    cnt = 0
    for j in a[1:]:
        if j > avg:
            cnt += 1
    cnt = (cnt / a[0]) * 100
    print('%.3f'%cnt+'%')