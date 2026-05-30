n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def abs(n, arr):
    for i in range(n):
        if arr[i] >= 0:
            continue
        elif arr[i] < 0:
            arr[i] *= -1
    print(*arr)

abs(n, arr)