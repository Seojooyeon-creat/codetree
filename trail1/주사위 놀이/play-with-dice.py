

count_arr = [0] * 7

arr = list(map(int, input().split()))
for elem in arr:
    count_arr[elem] += 1
for j in range(1, 7):
    cnt = count_arr[j]
    print(f"{j} - {cnt}")
