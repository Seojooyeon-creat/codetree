A = []  # 전역 변수

N, M = map(int, input().split())

A = [0] + list(map(int, input().split()))

prefix = [0] * (N + 1)

for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + A[i]

for _ in range(M):
    a1, a2 = map(int, input().split())
    print(prefix[a2] - prefix[a1 - 1])