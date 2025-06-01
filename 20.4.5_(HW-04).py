import json

# Загрузка данных из файла
with open("orders_july_2023.json", "r") as file:
    orders = json.load(file)

# 1. Какой номер самого дорогого заказа за июль?
max_price = 0
max_price_order = None
for order_num, order_data in orders.items():
    if order_data['price'] > max_price:
        max_price = order_data['price']
        max_price_order = order_num

# 2. Какой номер заказа с самым большим количеством товаров?
max_quantity = 0
max_quantity_order = None
for order_num, order_data in orders.items():
    if order_data['quantity'] > max_quantity:
        max_quantity = order_data['quantity']
        max_quantity_order = order_num

# 3. В какой день в июле было сделано больше всего заказов?
from collections import defaultdict
orders_per_day = defaultdict(int)
for order_data in orders.values():
    orders_per_day[order_data['date']] += 1
max_orders_day = max(orders_per_day.items(), key=lambda x: x[1])[0]

# 4. Какой пользователь сделал самое большое количество заказов за июль?
user_orders_count = defaultdict(int)
for order_data in orders.values():
    user_orders_count[order_data['user_id']] += 1
max_orders_user = max(user_orders_count.items(), key=lambda x: x[1])[0]

# 5. У какого пользователя самая большая суммарная стоимость заказов за июль?
user_total_spent = defaultdict(int)
for order_data in orders.values():
    user_total_spent[order_data['user_id']] += order_data['price']
max_spent_user = max(user_total_spent.items(), key=lambda x: x[1])[0]

# 6. Какая средняя стоимость заказа была в июле?
total_orders = len(orders)
total_price = sum(order_data['price'] for order_data in orders.values())
average_order_price = total_price / total_orders

# 7. Какая средняя стоимость товаров в июле?
total_quantity = sum(order_data['quantity'] for order_data in orders.values())
average_item_price = total_price / total_quantity

# Вывод результатов
print(f"1. Номер самого дорогого заказа за июль: {max_price_order}")
print(f"2. Номер заказа с самым большим количеством товаров: {max_quantity_order}")
print(f"3. День с наибольшим количеством заказов: {max_orders_day}")
print(f"4. Пользователь с наибольшим количеством заказов за июль: {max_orders_user}")
print(f"5. Пользователь с самой большой суммарной стоимостью заказов за июль: {max_spent_user}")
print(f"6. Средняя стоимость заказа в июле: {average_order_price:.2f}")
print(f"7. Средняя стоимость товаров в июле: {average_item_price:.2f}")