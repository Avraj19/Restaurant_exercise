class Order():

    def __init__(self, customer):
        self.order_items =[]
        self.customer = customer
        self.status = 'open'

    def add_item_order(self, order_item):
        self.order_items.append(order_item)