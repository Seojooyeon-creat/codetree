n = int(input())

# Please write your code here.

def prin(n):
    if n == 0:
        return

    for i in range(1, n+1):
        print(i, end = " ")
    print(" ")
    for i in range(n, 0, -1):
        print(i, end = " ")
prin(n)
