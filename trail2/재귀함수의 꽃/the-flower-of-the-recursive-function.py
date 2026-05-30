N = int(input())

# Please write your code here.

def prin(n):

    for j in range(n, 0, -1):
        print(j, end = " ")

    for i in range(1, n + 1):
        print(i, end = " ")
 
   
prin(N)