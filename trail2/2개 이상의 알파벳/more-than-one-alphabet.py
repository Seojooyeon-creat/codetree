A = input()

# Please write your code here.

def dif(a):
    count = 0
    k = list(a)
    for i in range(len(k)):
        if k[i] == k[i - 1]:
            count += 1
    
    if count == len(k):
        print("No")
    else:
        print("Yes")

dif(A)