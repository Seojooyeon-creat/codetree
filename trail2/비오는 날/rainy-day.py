n = int(input())
fore = []
rain = []

# Please write your code here.

class forecast:
    def __init__(self, d, dy, w):
        self.d = d
        self.dy = dy
        self.w = w


for _ in range(n):
    d, dy, w = input().split()
    fore.append(forecast(d, dy, w))

for f in fore:
    if f.w == "Rain":
        rain.append([f.d, f.dy, f.w])

rain.sort()
print(*rain[0])
        





        
    