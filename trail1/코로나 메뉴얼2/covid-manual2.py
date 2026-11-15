arr=[]
for i in range(3):
    arr.append((input().split()))

count = [0] * 4

for elem in arr:
    if elem[0] == "Y" and int(elem[1]) >= 37:
        count[0] += 1
    elif elem[0] == "N" and int(elem[1]) >= 37:
        count[1] += 1
    elif elem[0] == "Y" and int(elem[1]) < 37:
        count[2] += 1
    elif elem[0] == "N" and int(elem[1]) < 37:
        count[3] += 1
if count[0] >= 2:
    count.append("E")
print(*count)