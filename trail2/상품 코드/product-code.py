product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.

class product:
    def __init__(self, pn = "codetree", pc = 50):
        self.pn = pn
        self.pc = pc

k = product()
print(f"product {k.pc} is {k.pn}")
s = product(product_name, product_code)
print(f"product {s.pc} is {s.pn}")

