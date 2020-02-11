from People_class import Peolpe
from Customers_sub_class import Customers
from Food_items_class import Food_items
from Combs_sub_class import Combos
from Orders_class import Order
# As a restaurant owner i can create customers.

customer_1 = Customers('John', '21 Down Town Adi, London')
customer_2 = Customers('Anabela', 'Hackney, London')

# as a restaurant owner i can create food items.
# 3 mains

main_1 = Food_items('Sea Bass', 17.5, ['Sea Bass fish'])
main_2 = Food_items('Omelet', 9, ['Eggs', 'Cheese', 'Mushrooms'])
main_3 = Food_items('Fiorentine', 5.5, ['Tomato', 'Mozzarella', 'Parmesan', 'Egg', 'Spinach'])

# 3 Sides

side_1 = Food_items('Garlic Bread', 4 , ['Bread', 'Gralic', 'Oregano'] )
side_2 = Food_items('Garlic Bread with cheese', 4, ['Bread','Cheese', 'Garlic', 'Oregano'])

# 3 drinks
drink_1 = Food_items('Water', 2, ['water'])
drink_2 = Food_items('Cocacola', 3, ['others'])
drink_3 = Food_items('Smoothies', 4, ['orange', 'carrots', 'kiwi'])

# as a restaurant owner i can create new orders with food.
# opening a tab to order

order_1 = Order(customer_1)

order_1.add_item_order((main_3))
order_1.add_item_order(drink_1)

print(order_1)
print(order_1.order_items)
# for items in order_1.order_items:
#     print()