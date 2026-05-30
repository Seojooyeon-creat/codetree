n = int(input())

# Please write your code here.

class summation:
    def __init__(self, name, s1, s2, s3):
        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

student = []
for _ in range(n):
    name, s1, s2, s3 = tuple(input().split())
    student.append(summation(name, int(s1), int(s2), int(s3)))

student.sort(key = lambda x : x.s1 + x.s2 + x.s3)

for i in student:
    print(i.name, i.s1, i.s2, i.s3)