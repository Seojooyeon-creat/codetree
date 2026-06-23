# 변수 선언 및 입력:
n = int(input())


def fibo(n):
    # 첫 번째, 두 번째 원소는 1입니다.
    if n <= 2:
        return 1
    
    # 3번째 원소부터는 다음 점화식을 만족합니다.
    return fibo(n - 1) + fibo(n - 2)


print(fibo(n))
