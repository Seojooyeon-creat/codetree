N = int(input())
for i in range(1, N + 1):
    stars = N - i + 1
    spaces = 2 * (i - 1)
    print("*" * stars + " " * spaces + "*" * stars)