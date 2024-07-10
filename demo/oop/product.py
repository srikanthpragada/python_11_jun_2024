class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"

    def __eq__(self, other):
        #print("__eq__")
        return self.name == other.name and self.price == other.price

    def __gt__(self, other):
        #print("__gt__")
        return self.price > other.price

    def __int__(self):
        return self.price


p1 = Product("iPhone 15", 100000)
p2 = Product("iPhone 15", 100000)
p3 = Product("iPhone 14", 80000)
print(p1)  # str(p1)  ->  p1.__str__()
print(str(p1))
print(int(p1))  # p1.__int__()


print(p1 == p2)  # p1.__eq__(p2)
print(p1 == p3)
print(p1 > p3)  # p1.__gt__(p3)
print(p1 < p3)

prods = [p1, p2, p3]

for p in sorted(prods):
    print(p)
