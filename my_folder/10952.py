# while True : 무한반복문, break가 오면 종료

while True:
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0:
        break

    print(a + b)
