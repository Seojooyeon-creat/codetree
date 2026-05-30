n = int(input())

# Please write your code here.

def prin(n):
    if n == 0:
        return

    print("* " * n)
    prin(n - 1)
    print("* " * n)

prin(n)