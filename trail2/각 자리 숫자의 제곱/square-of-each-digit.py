N = int(input())

# Please write your code here.

def seat(N):
    
    if N < 10:
        return N * N
    
    digit = ( N % 10)
    return seat(N // 10) + digit * digit
    
   

print(seat(N))



