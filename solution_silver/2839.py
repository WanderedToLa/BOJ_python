n = int(input())
bag = 0
a = 0

if n % 5 == 0:
    bag += n // 5
    print(bag)
elif n % 5 == 1 or n % 5 == 2 or n % 5 == 4:
    bag += (n // 5)
    a += n % 5
    if a != 0:
        while True:
            bag -= 1
            a += 5
            if a % 3 == 0:
                a = a // 3
                if bag < 0:
                    print(-1)
                    break
                bag = a + bag
                print(bag)
                break
            elif bag < 0:
                print(-1)
                break
elif n % 5 == 3:
    bag += (n // 5) + 1
    print(bag)
elif n % 3 == 0:
    bag += n // 3
    print(bag)