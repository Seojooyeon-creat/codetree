n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

def dmp(n, m, arr):
    lst = []
    lst.append(arr[0])
    while m != 1:
        lst.append(arr[m - 1])
        if m % 2 == 1:
            m -= 1
        else:
            m //= 2
        
    return lst

lst = dmp(n, m, A)
print(sum(lst))

