arr = []

for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr) # 중복을 제거

print(len(arr)) # 중복을 뺀 길이 출력