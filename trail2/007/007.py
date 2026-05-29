secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.

class zero:
    def __init__(self, se, me, time):
        self.se = se
        self.me = me
        self.time = time
    
s = zero(secret_code, meeting_point, time)

print(f"secret code : {s.se}")
print(f"meeting point : {s.me}")
print(f"time : {s.time}")
        