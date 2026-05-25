n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
upper = sorted(nums)
downer = reversed(upper)

print(*upper)
print(*downer)