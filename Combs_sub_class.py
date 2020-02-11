from Food_items_class import Food_items


class Combos(Food_items):

    def __int__(self, item, price, list_individual_items=None, ingredients=None):
        super().__init__(item, price, ingredients=None)
        if list_individual_items is None:
            list_individual_items = []
        self.list_individual_item = list_individual_items
