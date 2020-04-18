class Product:
    def __init__(self, price):
        self.set_price(price)

    # def get_price(self):
    #     return self.price

    def set_price(self, price):
        if price < 0:
            raise ValueError("NO")
        self.price = price

    def draw(self):
        print(self.price)


h = Product(4)
h.draw()
