n = int(input())
newNum = n
count = 0

while True:
    m = newNum // 10
    l = newNum % 10
    k = (m + l) % 10
    newNum = (l * 10) + k
    count += 1
    if (newNum == n):
        break
print(count)