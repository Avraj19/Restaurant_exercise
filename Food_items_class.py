class Food_items:

    def __int__(self, item, price, ingredients=None):
        self.item = item
        self.price = price

        if ingredients is None:
            ingredients = []
        self.ingredients = ingredients
