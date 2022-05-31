t = int(input())

for i in range(t):
    n , s = input().split()
    text = ''
    for j in s:
        text += int(n) * j
    print(text)