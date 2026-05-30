n = int(input())

# Please write your code here.

student = []

class hw:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

for _ in range(n):
    name, h, w = tuple(input().split())
    student.append(hw(name, int(h), int(w)))

student.sort(key = lambda x : (x.h, -x.w, x.name))

for i in student:
    print(i.name, i.h, i.w)