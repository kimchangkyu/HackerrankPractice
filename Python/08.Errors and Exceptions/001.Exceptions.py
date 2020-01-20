N = int(input())

for _ in range(N):
    num1, num2 = map(str, input().split())

    try:
        result = int(num1) // int(num2)
        print(int(result))
    except ZeroDivisionError as e:
        print('Error Code:', e)
    except ValueError as e:
        print('Error Code:', e)