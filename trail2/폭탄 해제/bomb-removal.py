unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.

class cable:
    def __init__(self, code, wc, sec):
        self.code = code
        self.wc = wc
        self.sec = sec

s = cable(unlock_code, wire_color, seconds)

print("code :",s.code)
print("color :",s.wc)
print("second :",s.sec)