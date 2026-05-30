n = 5

# Please write your code here.
person = []
class pi:
    def __init__(self, name, t, w):
        self.name = name
        self.t = t
        self.w = w

for _ in range(n):
    name, t, w = tuple(input().split())
    person.append(pi(name, int(t), float(w)))
person.sort(key = lambda x : x.name)

print("name")

for i in person:
    print(i.name, i.t, i.w)
print("")
person.sort(key = lambda x : -x.t)
print("height")

for i in person:
    print(i.name, i.t, i.w)
