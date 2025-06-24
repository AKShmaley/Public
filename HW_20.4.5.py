import json

with open("translator.json", "r", encoding="utf-8") as file:
    orders = json.load(file)

max_price = 0
max_price_orders = []

max_quantity = 0
max_quantity_orders = []

orders_per_day = {}
orders_per_user = {}
total_price_per_user = {}

total_price = 0
total_quantity = 0
total_orders = 0

for order_num, order in orders.items():
    date = order['date']
    user = order['user_id']
    quantity = order['quantity']
    price = order['price']

    if price > max_price:
        max_price = price
        max_price_orders = [order_num]
    elif price == max_price:
        max_price_orders.append(order_num)

    if quantity > max_quantity:
        max_quantity = quantity
        max_quantity_orders = [order_num]
    elif quantity == max_quantity:
        max_quantity_orders.append(order_num)

    orders_per_day[date] = orders_per_day.get(date, 0) + 1

    orders_per_user[user] = orders_per_user.get(user, 0) + 1

    total_price_per_user[user] = total_price_per_user.get(user, 0) + price

    total_price += price
    total_quantity += quantity
    total_orders += 1

print(f"Номера самых дорогих заказов (цена = {max_price}): {', '.join(max_price_orders)}")

print(f"Номера заказов с наибольшим количеством товаров (кол-во = {max_quantity}): {', '.join(max_quantity_orders)}")

max_orders_per_day = max(orders_per_day.values())
top_days = [d for d, count in orders_per_day.items() if count == max_orders_per_day]
print(f"Дни с наибольшим числом заказов ({max_orders_per_day} заказов): {', '.join(top_days)}")

other_days = [d for d, count in orders_per_day.items() if count != max_orders_per_day]
print(f"Остальных дней, где не {max_orders_per_day} заказов: {len(other_days)}")

max_user_orders = max(orders_per_user.values())
top_users = [u for u, count in orders_per_user.items() if count == max_user_orders]
print(f"Пользователи с наибольшим числом заказов ({max_user_orders} заказов): {', '.join(map(str, top_users))}")

max_user_spending = max(total_price_per_user.values())
top_spenders = [u for u, total in total_price_per_user.items() if total == max_user_spending]
print(f"Пользователи с самой большой суммой заказов ({max_user_spending}): {', '.join(map(str, top_spenders))}")

avg_order_price = total_price / total_orders
print(f"Средняя стоимость заказа: {avg_order_price:.2f}")

avg_item_price = total_price / total_quantity if total_quantity else 0
print(f"Средняя стоимость одного товара: {avg_item_price:.2f}")
