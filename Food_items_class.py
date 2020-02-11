class Food_items():

    def __init__(self, item, price, ingredients=None):
        if ingredients is None:
            ingredients = []
        self.ingredients = ingredients
        self.item = item
        self.price = price


