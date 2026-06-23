N = int(input())

# Please write your code here.

def pr(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    



    return pr(n - 2) + n

print(pr(N))