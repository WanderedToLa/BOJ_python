N , M = map(int,input().split())
firstArr = set()
SecondArr = set()

for _ in range(N):
    firstArr.add(input())
for _ in range(M):
    SecondArr.add(input())

Array = sorted(list(firstArr & SecondArr))
print(len(Array))

for i in Array:
    print(i)