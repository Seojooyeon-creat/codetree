n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
aset = set(A)
bset = set(B)

if aset == bset:
    print("Yes")
else:
    print("No")