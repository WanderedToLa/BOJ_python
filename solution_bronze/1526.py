n = int(input())

while True:
    tool = True
    for i in str(n):
        if i != "4" and i != "7":
            tool = False
            n -= 1
    if tool :
        print(n)
        break