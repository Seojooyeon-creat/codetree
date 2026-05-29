user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.

class game:
    def __init__(self, id = "codetree", level = 10):
        self.id = id
        self.level = level


u1 = game()
print("user", u1.id, "lv", u1.level)
u2 = game(user2_id, user2_level)
print("user", u2.id, "lv", u2.level)
    
