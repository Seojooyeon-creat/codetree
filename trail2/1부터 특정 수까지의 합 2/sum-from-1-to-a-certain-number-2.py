N = int(input())

# Please write your code here.

def summation(N):
    if N == 1:
        return 1
    return summation(N - 1) + N

print(summation(N))