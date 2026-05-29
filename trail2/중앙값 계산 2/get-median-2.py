n = int(input())
nums = list(map(int, input().split()))

result = []
current = []

for i, num in enumerate(nums):
    current.append(num)
    if (i + 1) % 2 == 1:
        current.sort()
        result.append(current[len(current) // 2])

print(*result)