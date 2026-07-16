fee = 10
free = 0

def delivery_fee(order_total):
    if order_total >= 50:
        total = order_total + free
        return (f"Order: {order_total} - Fee: {free} - Total: {total}")
    else:
        total = order_total + fee
        return (f"Order: {order_total} - Fee: {fee} - Total: {total}")

print(delivery_fee(35))
print(delivery_fee(60))
print(delivery_fee(48))
