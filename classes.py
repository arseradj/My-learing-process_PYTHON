# class Reza:
#     # @classmethod
#     # def jigar(cls):
#     #     return cls(0, 2)

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # def __add__(self, other):
#     #     return Reza(self.x+other.x, self.y+other.y)

#     # def __eq__(self, other):
#     #     return self.x == other.x and self.y == other.y

#     def bekesh(self):
#         print(f'{self.x}, {self.y}')


# f = Reza(2, 3)
# f.bekesh()
# f.z = 10
# print(f.x)
# g = Reza.jigar()
# g.bekesh()
# h = Reza.jigar()
# h.bekesh()
# print(g == h)
# x = h+g
# x.bekesh()

# class Reza:
#     def __init__(self):
#         self.x = []

#     def append(self, num):
#         self.x.append(num+1+5*4)

#     def bekesh(self):
#         print(self.x)

#     def __eq__(self, other):
#         return self.x == other.x


# h = Reza()
# h.append(1)
# h.append(0)
# g = Reza()
# g.append(1)
# g.append(0)
# h.bekesh()
# g.bekesh()
# print(g == h)

# class Reza:
#     #     # @classmethod
#     #     # def jigar(cls):
#     #     #     return {"reza": 1, "seradj": 2}

#     def __init__(self):
#         self.x = {}

#     def add(self, esm):
#         self.x[esm.lower()] = self.x.get(esm.lower(), 0)+1

#     def __getitem__(self, esm):
#         return self.x.get(esm.lower(), 0)

#     def __setitem__(self, esm, count):
#         self.x[esm.lower()] = count

#     def __len__(self):
#         return len(self.x)


# #     def __getitem__(self, esm):
# #         return self.x.get(esm.lower(), 0)

# #     # def bekesh(self):
# #     #     print(self.x)

# #     # def __eq__(self, other):
# #     #     return self.x == other

# h = Reza()
# h.add("reza")
# h.add("seradj")
# h.add("seradj")
# h.add("red")
# h.add("dd")
# print(h["dd"])
# # h.append(1)
# # h.append(0)

class Kharid:
    def __init__(self, price):
        self.item = price

    @property
    def price(self):
        return self.item

    @price.setter
    def price(self, gheymat):
        if gheymat < 0:
            raise ValueError("NO NO NO")
        self.item = gheymat


list = Kharid(10)
list.price = -10
print(list.price)
