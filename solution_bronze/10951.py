while True:
    try:
        a , b = map(int , input().split()) # a b를 계속 입력받음
    except:
        break # 값이 입력되지않으면 반복문 탈출
    print(a + b)