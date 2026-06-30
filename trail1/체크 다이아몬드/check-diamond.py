N = int(input())
for i in range(1, 2 * N):
    cnt = i if i <= N else 2 * N - i
    print(" " * (N - cnt) + " ".join("*" * cnt))